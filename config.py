import os


class DevConfig:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:testbase@localhost/spooderman'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    USE_RELOADER = False
    ENV = 'development'
