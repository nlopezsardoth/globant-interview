import datetime

class WeatherDataTransformer:
    def __init__(self, weather_data, city, country):
        self.weather_data = weather_data
        self.city = city
        self.country = country

    def transform_data(self):
        transformed_data = {
            "location_name": f"{self.city, self.country}",
            "temperature": f"{self.kelvin_to_celsius(self.weather_data['current']['temp'])}°C / {self.kelvin_to_fahrenheit(self.weather_data['current']['temp'])}°F",
            "wind": self.format_wind_data(self.weather_data['current']),
            "cloudiness": self.weather_data['current']['weather'][0]['description'],
            "pressure": f"{self.weather_data['current']['pressure']} hpa",
            "humidity": f"{self.weather_data['current']['humidity']}%",
            "sunrise": self.unix_to_time(self.weather_data['current']['sunrise']),
            "sunset": self.unix_to_time(self.weather_data['current']['sunset']),
            "geo_coordinates": f"[{self.weather_data['lat']}, {self.weather_data['lon']}]",
            "requested_time": datetime.datetime.fromtimestamp(self.weather_data['current']['dt']).strftime("%Y-%m-%d %H:%M:%S"),
            "forecast": self.transform_forecast(),
        }
        return transformed_data

    def kelvin_to_celsius(self, kelvin):
        return round(kelvin - 273.15, 1)
    
    def kelvin_to_fahrenheit(self, kelvin):
        celsius = self.kelvin_to_celsius(kelvin)
        fahrenheit = (celsius * 9/5) + 32
        return round(fahrenheit, 1)

    def format_wind_data(self, data):
        speed = round(data['wind_speed'] * 3.6, 1)
        direction = self.wind_direction_to_text(data['wind_deg'])
        return f"{speed} km/h, {direction}"

    def wind_direction_to_text(self, degrees):
        return ["north","north-northeast","northeast","east-northeast","east","east-southeast", "southeast", "south-southeast","south","south-southwest","southwest","west-southwest","west","west-northwest","northwest","north-northwest"][round(degrees/22.5)%16]

    def unix_to_time(self, unix_timestamp):
        return datetime.datetime.fromtimestamp(unix_timestamp).strftime("%H:%M")
    
    def transform_forecast(self):
        transformed_data = {
            "temperature": f"{self.kelvin_to_celsius(self.weather_data['daily'][0]['temp']['day'])}°C / {self.kelvin_to_fahrenheit(self.weather_data['current']['temp'])}°F",
            "wind": self.format_wind_data(self.weather_data['daily'][0]),
            "cloudiness": f"{self.weather_data['daily'][0]['weather'][0]['description']}",
            "pressure": f"{self.weather_data['daily'][0]['pressure']} hpa",
            "humidity": f"{self.weather_data['daily'][0]['humidity']}%",
            "sunrise": self.unix_to_time(self.weather_data['daily'][0]['sunrise']),
            "sunset": self.unix_to_time(self.weather_data['daily'][0]['sunset']),
        }
        return transformed_data
    
