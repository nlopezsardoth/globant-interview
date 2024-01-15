import requests
from flask import jsonify, make_response, request, current_app
from app.weather import bp

from .exceptions import PositionDataRetrievalError, WeatherDataRetrievalError, PositionDataError
from .errors import build_error_response

from .utils.get_weather_data import get_weather_data

from cache import cache

@bp.route('/weather', methods=["GET"])
def get_weather():
    API_KEY =  current_app.config["API_KEY"]

    city = request.args.get("city")
    country = request.args.get("country")

    if not city or not country:
        return make_response(jsonify({'error': 'Missing city or country'}), 400)
    
    if not city.isalpha() :
        return make_response(jsonify({'error': 'Invalid city name'}), 400)

    if not country.isalpha() or len(country)>2:
        return  make_response(jsonify({'error': 'Invalid country name'}), 400)

    try:
        
        weather_data = get_weather_data(city_name=city, country=country, api_key=API_KEY)
        
    except (PositionDataRetrievalError, WeatherDataRetrievalError, PositionDataError) as e:
        return build_error_response(str(e))  # Handle custom exceptions
    except Exception as e:
        current_app.logger.error(f"Unexpected error: {e}")  # Log unexpected errors
        return build_error_response("An unexpected error occurred")
    else:
        cache.set("weather_data", jsonify(weather_data)) #cache weather data
        return jsonify(weather_data), 200  # Return weather data on success