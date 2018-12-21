from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_redis import FlaskRedis


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    # set db
    db = SQLAlchemy()
    redis_store = FlaskRedis()

    with app.app_context():
        db.init_app(app)

        # Set global contexts
        redis_store.uri = app.config['SQLALCHEMY_DATABASE_URI']
        redis_store.gettoken = app.config['GET_TOKEN_ENDPOINT']
        redis_store.listviews = app.config['LIST_VIEWS_ENDPOINT']
        redis_store.getview = app.config['GET_VIEW_ENDPOINT']
        # CREDENTIALS
        redis_store.user = app.config['USER']
        redis_store.password = app.config['PASSWORD']
        # Initialize with vars
        redis_store.init_app(app)

        # Construct the data set
        from . import routes

        return app
