import requests
from flask import current_app, make_response, jsonify

from .weather_data_transformer import WeatherDataTransformer


    

def get_position(city_name, country):
    API_KEY =  current_app.config["API_KEY"]
    try:
        resp = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city_name},{country}&appid={API_KEY}")
        resp.raise_for_status()
        data = resp.json()
        coordinates = data.get("coord")
        lat, lon, country, city = coordinates["lat"],  coordinates["lon"], data.get("sys")["country"], data.get("name")
        return lat, lon, country, city
    except requests.exceptions.RequestException as e:
        return make_response(jsonify({'error': 'Failed to fetch position data'}), 500)

def get_weather_data(lat, lon, city_name, country):
    API_KEY =  current_app.config["API_KEY"]
    try:
        resp = requests.get(f"http://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={API_KEY}")
        resp.raise_for_status()
        weather_data = resp.json()
        transformer = WeatherDataTransformer(weather_data=weather_data, city=city_name, country=country)
        transformed_data = transformer.transform_data()
        return transformed_data

    except requests.exceptions.RequestException as e:
        return make_response(jsonify({'error': 'Failed to fetch weather data'}), 500)
