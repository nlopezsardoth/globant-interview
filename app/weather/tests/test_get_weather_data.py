import unittest

from .test_config import TestConfig
from app.weather.utils.get_weather_data import get_weather_data
from ..exceptions import PositionDataRetrievalError, WeatherDataRetrievalError, PositionDataError

class TestGetWeatherData(unittest.TestCase):

    def test_get_weather_data_normal(self):
            weather_data = get_weather_data(city_name="bogota", country="co", api_key=TestConfig.API_KEY)
            assert "cloudiness" in weather_data.keys()

    def test_get_position_invalid_city(self):
        with self.assertRaises(PositionDataRetrievalError):
            get_weather_data(city_name="medelllllin", country="co", api_key=TestConfig.API_KEY)




