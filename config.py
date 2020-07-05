import os
from os import environ

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = environ.get('SECRET_KEY') or 'you-will-never-guess'
    API_KEY = environ.get('API_KEY')

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') \
                              or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
