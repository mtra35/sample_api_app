from flask import Flask
from flask_restful import Api
from .main.routes import initialize_routes


def create_app():
    # Init app and api
    app = Flask(__name__)
    api = Api(app)

    initialize_routes(api)

    return app
