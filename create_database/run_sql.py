import os
import pymysql
from sqlalchemy import create_engine
from configparser import ConfigParser


def get_config():
    cp = ConfigParser()
    cp.read('config/config.cfg')
    try:
        return (
            'mysql+pymysql://'
            + cp.get('mysql', 'username')
            + ':'
            + cp.get('mysql', 'password')
            + '@'
            + cp.get('mysql', 'host')
            + ':'
            + cp.get('mysql', 'port')
            + '/'
            + cp.get('mysql', 'database')
            + '??charset='
            + cp.get('mysql', 'encoding')
        )
    except Exception as e:
        print(e)


def create_connection():
    return create_engine(get_config())


def connect_mysql():
    cp = ConfigParser()
    cp.read('config/config.cfg')
    try:
        conn = pymysql.connect(
            host=cp.get('mysql', 'host'),
            user=cp.get('mysql', 'username'),
            password=cp.get('mysql', 'password'),
            db=cp.get('mysql', 'database'),
            charset='utf8',
        )
        return conn
    except pymysql.err.OperationalError as e:
        print('Error is ' + str(e))


def run_sqlite():
    try:
        os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.utf8'
        engine = create_connection()
        ##读取SQL文件,获得sql语句的list
        with open(u'config/textLabel.sql', 'r+') as f:
            sql_list = f.read().split(';')[:-1]  # sql文件最后一行加上;
            sql_list = [
                x.replace('\n', ' ') if '\n' in x else x for x in sql_list
            ]  # 将每段sql里的换行符改成空格
        ##执行sql语句，使用循环执行sql语句
        with engine.connect() as conn:
            for sql_item in sql_list:
                conn.execute(sql_item)
    except Exception as e:
        print(e)

