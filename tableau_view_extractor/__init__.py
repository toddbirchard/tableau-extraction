"""Initialize application."""
from flask import Flask
from flask_redis import FlaskRedis
from flask_sqlalchemy import SQLAlchemy

# Set global entities
db = SQLAlchemy()
r = FlaskRedis()


def create_app():
    """Initialize Flask app UI."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")

    with app.app_context():
        # Initiate globals
        db.init_app(app)
        r.init_app(app)

        # Set global contexts
        r.set("uri", app.config["SQLALCHEMY_DATABASE_URI"])
        r.set("baseurl", app.config["REDIS_HOST"])
        r.set("username", app.config["REDIS_USERNAME"])
        r.set("password", app.config["REDIS_PASSWORD"])

        # Import our modules
        from . import routes

        app.register_blueprint(routes.home_blueprint)

        return app
