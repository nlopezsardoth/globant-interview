from flask import Blueprint

bp = Blueprint('wheather', __name__)

from app.weather import routes