from web import create_app, db

from flask_restx import Api
from flask import Blueprint
from web.controller.routes import route as route_ns

blueprint = Blueprint('url', __name__)

url = Api(blueprint,
          title = 'it is a title',
          version = '1.0',
          description = 'url shortener api')

url.add_namespace(route_ns, path = '/api')

app = create_app()
app.register_blueprint(blueprint)

if __name__ == "__main__":
    db.create_all()
    app.run(debug = True)