from flask import Flask
from flask_restful import Api
from .main.routes import initialize_routes
from .main.errors import errors


def create_app():
    # Init app and api
    app = Flask(__name__)
    api = Api(app, errors=errors)

    initialize_routes(api)

    return app
