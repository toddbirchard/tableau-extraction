from flask import Flask, g
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
        # Set up variables to be used globally
        db.init_app(app)
        r.init_app(app, charset="utf-8", decode_responses=True)

        # Set global contexts
        r.set('uri', app.config['SQLALCHEMY_DATABASE_URI'])
        r.set('gettoken', app.config['GET_TOKEN_ENDPOINT'])
        r.set('listviews', app.config['LIST_VIEWS_ENDPOINT'])
        r.set('getview', app.config['GET_VIEW_ENDPOINT'])
        r.set('baseurl',  app.config['BASE_URL'])
        r.set('username',  app.config['USERNAME'])
        r.set('password', app.config['PASSWORD'])
        r.set('contenturl', app.config['CONTENT_URL'])

        # Construct the data set
        from . import routes
        from . import tableau
        app.register_blueprint(routes.home_blueprint)
        # app.register_blueprint(view_dash.view_blueprint)
        # dash_app = view_dash.Add_Dash(app)

        return app
