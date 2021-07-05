import os
import pymysql
from sqlalchemy import create_engine
from configparser import ConfigParser


def get_config():
    """获取配置文件中的配置参数

    Return:
        :mysql config string(str): 返回一串包含连接MySQL所需要的所有参数字符串
    """
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
    """创建一个连接引擎

    Return:加入配置的引擎对象（Engine）
    """
    return create_engine(get_config())


def connect_mysql():
    """连接MySQL
    
    Return:
        :成功连接MySQL的Connection对象（Connection）
    """
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
    """运行SQL脚本，创建数据库及相关表
    """
    try:
        os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.utf8'
        engine = create_connection()
        with open(u'config/textLabel.sql', 'r+') as f:  # 读取SQL文件,获得sql语句的list
            sql_list = f.read().split(';')[:-1]  # sql文件最后一行加上;
            sql_list = [
                x.replace('\n', ' ') if '\n' in x else x for x in sql_list
            ]  # 将每段sql里的换行符改成空格
        with engine.connect() as conn:  # 执行sql语句，使用循环执行sql语句
            for sql_item in sql_list:
                conn.execute(sql_item)
    except Exception as e:
        print(e)

