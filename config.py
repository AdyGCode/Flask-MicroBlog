import os
from os import environ

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = environ.get('SECRET_KEY') or 'you-will-never-guess'
    API_KEY = environ.get('API_KEY')

    POSTS_PER_PAGE = int(environ.get('POSTS_PER_PAGE') or 3)

    SQLALCHEMY_DATABASE_URI = environ.get('DATABASE_URL') \
                              or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER = environ.get('MAIL_SERVER')
    MAIL_PORT = int(environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = environ.get('MAIL_PASSWORD')
    ADMINS = ['admin@example.com']
