from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():

    app = Flask(__name__)
    app.config.from_pyfile('settings.py')
    db.init_app(app)
    app.app_context().push()
    from .controller import routes
    app.register_blueprint(routes, url_prefix = "/")
    return app
