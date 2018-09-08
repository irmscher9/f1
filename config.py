import os

class Config(object):
    # SECRET_KEY = os.environ.get('123') or 'you-will-never-guess'

    # secret key
    SECRET_KEY = '5e644abffe28e6b1f7a99c0632360ffb'

    # database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///one.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
