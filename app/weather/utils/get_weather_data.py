import requests

from .weather_data_transformer import WeatherDataTransformer

from ..exceptions import PositionDataRetrievalError, WeatherDataRetrievalError, PositionDataError


def _fetch_position_data(city_name, country, api_key):
    """Retrieves position data from the API."""
    try:
        resp = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city_name},{country}&appid={api_key}")
        resp.raise_for_status()
        return resp.json()
    except requests.exceptions.RequestException as e:
        raise PositionDataRetrievalError(f"Failed to fetch position data: {e.response.text}") from e
    
def _get_position(city_name, country, api_key):
    """Extracts position data from API response."""
    try:
        data = _fetch_position_data(city_name, country, api_key)
        coordinates = data.get("coord")
        if coordinates:
            lat, lon = coordinates["lat"], coordinates["lon"]
            country = data.get("sys")["country"]
            city = data.get("name")
            return lat, lon, country, city
        else:
            raise PositionDataError("Missing coordinates in API response")
    except PositionDataRetrievalError as e:
        raise 
    except Exception as e:
        raise PositionDataError("Error processing position data") from e
    
def _fetch_weather_data(lat, lon, api_key):
    """Retrieves weather data from the API."""
    try:
        resp = requests.get(f"http://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={api_key}")
        resp.raise_for_status()
        return resp.json()

    except requests.exceptions.RequestException as e:
        raise WeatherDataRetrievalError("Failed to fetch weather data:  {e.response.text}") from e
    

def get_weather_data(city_name, country, api_key):
    try:
        lat, lon, country, city = _get_position(city_name, country, api_key)
        weather_data = _fetch_weather_data(lat, lon, api_key)
        transformer = WeatherDataTransformer(weather_data=weather_data, city=city, country=country)
        transformed_data = transformer.transform_data()
        return transformed_data

    except (PositionDataRetrievalError, PositionDataError, WeatherDataRetrievalError )as e:
        raise 
    except Exception as e:
        raise PositionDataError("Error processing weather data") from e
    
    
