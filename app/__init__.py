from flask import Flask
from config import Config
from cache import cache


def create_app(config_class =Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from app.weather import bp as weather
    app.register_blueprint(weather)

    cache.init_app(app)
    
    @app.route("/", methods=["GET"])
    def index():
        return "<h1> Go to /wheather </h1>"

    
    return app

