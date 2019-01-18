from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis

# Set global entities
db = SQLAlchemy()
r = FlaskRedis()


def create_app():
    """Construct the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    with app.app_context():
        # Initiate globals
        db.init_app(app)
        r.init_app(app, charset="utf-8", decode_responses=True)

        # Set global contexts
        r.set('uri', app.config['SQLALCHEMY_DATABASE_URI'])
        r.set('baseurl',  app.config['BASE_URL'])
        r.set('username',  app.config['USERNAME'])
        r.set('password', app.config['PASSWORD'])

        # Import our modules
        from . import routes
        app.register_blueprint(routes.home_blueprint)

        return app
