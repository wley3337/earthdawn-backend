import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    FLASK_ENV = os.environ['FLASK_ENV']
    JWT_COOKIE_SECURE = True
    JWT_SECRET_KEY = os.environ['JWT_SECRET_KEY']
    JWT_TOKEN_LOCATION = ["cookies"]
    PYTHONPATH = '.'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URI']
    TESTING = False


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = False
    DEVELOPMENT = True
    JWT_COOKIE_SECURE = False


class TestingConfig(Config):
    TESTING = True
