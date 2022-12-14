import os

postgresql = {'host': os.environ["MASTER_DB_HOST"],
              'user': os.environ["MASTER_DB_USER"],
              'passwd': os.environ["MASTER_DB_PASSWORD"],
              'db': os.environ["MASTER_DB_NAME"]}

postgresqlConfig = "postgresql+psycopg2://{}:{}@{}/{}".format(
    postgresql['user'], postgresql['passwd'], postgresql['host'], postgresql['db'])


class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ["SQLALCHEMY_TRACK_MODIFICATIONS"]
    TESTING = os.environ["TESTING"]
    DEBUG = os.environ["DEBUG"]
    FLASK_ENV = os.environ["FLASK_ENV"]
    JWT_SECRET_KEY = os.environ["JWT_SECRET_KEY"]
    MASTER_DB_HOST = os.environ["MASTER_DB_HOST"]
    MASTER_DB_USER = os.environ["MASTER_DB_USER"]
    MASTER_DB_PASSWORD = os.environ["MASTER_DB_PASSWORD"]
    MASTER_DB_NAME = os.environ["MASTER_DB_NAME"]