from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from config import app_config
from flask_migrate import Migrate


db = SQLAlchemy()
ma = Marshmallow()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    db.init_app(app)
    Migrate(app, db)

    from app import models

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint)

    return app


