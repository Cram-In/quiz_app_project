import os


class Config(object):
    DEBUG = os.environ.get("BUG_SET")
    DEVELOPMENT = os.environ.get("DEV_SET")
    FLASK_HTPASSWD_PATH = "/secret/.htpasswd"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SECRET_KEY = "do-i-really-need-this"