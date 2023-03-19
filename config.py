"""Configure Tableau Server Client & target SQL database."""
from os import environ, getenv, path

from dotenv import load_dotenv

BASE_DIR = path.abspath(path.dirname(__file__))
load_dotenv(path.join(BASE_DIR, ".env"))


class Config:
    """Parse config values from .ini."""

    # Testing vars
    FLASK_DEBUG = True
    TESTING = True
    # Assets
    FLASK_ASSETS_USE_CDN = True
    # Database
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    # Redis
    REDIS_URL = environ.get("REDIS_URL")
    REDIS_USERNAME = environ.get("REDIS_USERNAME")
    REDIS_PASSWORD = environ.get("REDIS_PASSWORD")
