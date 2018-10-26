from config import Config
from flask import Flask


def create_app(config_class=Config):
    app = Flask(__name__)
    print("creating")

    @app.route('/')
    def hello():
        return "Hello World!"

    return app
