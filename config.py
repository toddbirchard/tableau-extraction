import os
from configparser import ConfigParser


class Config:
    """Parse config values from .ini."""

    configParser = ConfigParser()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    configFilePath = (os.path.join(dir_path, 'config.ini'))
    configParser.read(configFilePath)

    # Testing vars
    DEBUG = True
    TESTING = True
    # Assets
    FLASK_ASSETS_USE_CDN = True
    # Database
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = configParser.get("DATABASE", "SQLALCHEMY_DATABASE_URI")
    REDIS_URL = configParser.get("DATABASE", "REDIS_URI")
    # CREDENTIALS
    BASE_URL = configParser.get("TABLEAU", "BASE_URL")
    USERNAME = configParser.get("TABLEAU", "USERNAME")
    PASSWORD = configParser.get("TABLEAU", "PASSWORD")
    CONTENT_URL = configParser.get("TABLEAU", "CONTENT_URL")
