from flask import jsonify, make_response, request
from app.weather import bp

from .utils.get_weather_data import get_position, get_weather_data

@bp.route('/wheather', methods=["GET"])
def get_weather():
    city = request.args.get("city")
    country = request.args.get("country")

    if not city or not country:
        return make_response(jsonify({'error': 'Missing city or country'}), 400)
    
    if not city.isalpha() :
        return make_response(jsonify({'error': 'Invalid city name'}), 400)

    if not country.isalpha()  and country.len>2:
        return  make_response(jsonify({'error': 'Invalid country name'}), 400)

    try:
        lat, lon, country, city = get_position("Bogota", "co")
        weather_data = get_weather_data(lat=lat, lon=lon, city_name=city, country=country)

        return make_response(jsonify(weather_data))
        
    except Exception as e:
        raise