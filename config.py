import os
from configparser import SafeConfigParser


class Config:
    """Parse config values from .ini."""

    configParser = SafeConfigParser()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    configFilePath = (os.path.join(dir_path, 'config.ini'))
    configParser.read(configFilePath)

    DEBUG = True
    TESTING = True
    # Endpoints
    GET_TOKEN_ENDPOINT = configParser.get("ENDPOINTS", "GET_TOKEN_ENDPOINT")
    GET_VIEW_ENDPOINT = configParser.get("ENDPOINTS", "GET_VIEW_ENDPOINT")
    LIST_VIEWS_ENDPOINT = configParser.get("ENDPOINTS", "LIST_VIEWS_ENDPOINT")
    # Database
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = configParser.get("DATABASE", "SQLALCHEMY_DATABASE_URI")
    # CREDENTIALS
    USER = configParser.get("CREDENTIALS", "USER")
    PASSWORD = configParser.get("CREDENTIALS", "PASSWORD")
