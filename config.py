import os

class Config:
    """Parse config values from .ini."""

    # Testing vars
    DEBUG = True
    TESTING = True
    # Assets
    FLASK_ASSETS_USE_CDN = True
    # Database
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    REDIS_URL = os.environ.get("REDIS_URI")
    # CREDENTIALS
    BASE_URL = os.environ.get("BASE_URL")
    USERNAME = os.environ.get("USERNAME")
    PASSWORD = os.environ.get("PASSWORD")
    CONTENT_URL = os.environ.get("CONTENT_URL")
