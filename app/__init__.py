from flask import Flask, request, jsonify, make_response, render_template
from config import Config


def create_app(config_class =Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from app.weather import bp as weather
    app.register_blueprint(weather)

    @app.route("/", methods=["GET"])
    def index():
        return "<h1> Go to /wheather </h1>"

    
    return app

