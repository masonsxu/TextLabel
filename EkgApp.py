import logging
import logging.handlers as handlers
from models.TextLabel_schema import LabelDatum
from gevent.pywsgi import WSGIServer
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, jsonify


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['TEMPLATES_AUTO_RELOAD'] = True
# 本地部署
# app.config[
#     'SQLALCHEMY_DATABASE_URI'
# ] = 'mysql+pymysql://root:12345678@localhost:3306/TextLabel_schema'
# 云服务器部署 lft
app.config[
    'SQLALCHEMY_DATABASE_URI'
] = 'mysql+pymysql://root:123456@localhost:3306/TextLabel_schema'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/get_text', methods=['GET'])
def get_text():
    if request.method == 'GET':
        try:
            labelData = (
                db.session.query(LabelDatum)
                .filter_by(abstract_label=None, label_flag=None)
                .first()
            )
            db.session.query(LabelDatum).filter_by(abstract=labelData.abstract).update(
                {LabelDatum.label_flag: 'labeling'}
            )
            db.session.commit()
            return jsonify({'abstract': labelData.abstract})
        except Exception:
            db.session.rollback()
            return jsonify({'abstract': None})


@app.route('/api/saveAndNext', methods=['POST'])
def saveAndNext():
    if request.method == 'POST':
        try:
            result = request.get_json()
            db.session.query(LabelDatum).filter(
                LabelDatum.abstract == str(result['abstract'])
            ).update({LabelDatum.abstract_label: str(result['abstract_label']),LabelDatum.label_flag: 'labeled'})
            labelData = (
                db.session.query(LabelDatum)
                .filter_by(abstract_label=None, label_flag=None)
                .first()
            )
            db.session.query(LabelDatum).filter_by(abstract=labelData.abstract).update(
                {LabelDatum.label_flag: 'labeling'}
            )
            db.session.commit()
            return jsonify({'abstract': labelData.abstract})
        except Exception:
            db.session.rollback()
            return jsonify({'abstract': None})


@app.route('/api/reset_label_flag', methods=['POST'])
def reset_label_flag():
    if request.method == 'POST':
        result = request.get_json()
        try:
            db.session.query(LabelDatum).filter(
                LabelDatum.abstract == str(result['abstract'])
            ).update({LabelDatum.label_flag: None})
            db.session.commit()
            return jsonify({'abstract': None})
        except Exception:
            db.session.rollback()
            return jsonify({'abstract': None})


@app.errorhandler(Exception)
def handle_exception_error(e):
    return render_template('index.html')


if __name__ == "__main__":
    """
    %(asctime)s 即日志记录时间，精确到毫秒
    %(levelname)s 即此条日志级别
    %(filename)s 即触发日志记录的python文件名
    %(funcName)s 即触发日志记录的函数名
    %(lineno)s 即触发日志记录代码的行号
    %(message)s 这项即调用如app.logger.info(‘info log’)中的参数，即message
    """
    from werkzeug.debug import DebuggedApplication

    logger = logging.getLogger('app')
    logger.setLevel(10)
    logger_format = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s'
    )
    logHandler = handlers.RotatingFileHandler(
        'log/flask.log', maxBytes=1000000, backupCount=1
    )
    logHandler.setFormatter(logger_format)
    logger.addHandler(logHandler)
    logger.info("Logging configuration done")
    dapp = DebuggedApplication(app, evalex=True)
    http_server = WSGIServer(('0.0.0.0', 5000), app, log=logger)
    print('======>>> App running at Local:   http://localhost:5000/<<<======')
    http_server.serve_forever()
