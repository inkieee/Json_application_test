import json

class InsertRedisData:
    """
    Class to insert weather data into Redis
    """
    def __init__(self, city, weather_data, r):
        """
        Initializes object to pass in weather data 

        Args:
            weather_data: Json data obtained from WeatherClient for a particular city   
        """
        self.city = city
        self.weather_data = weather_data
        self.r = r

    def insert_weather_data(self):
        """
        Inserts weather data into Redis object

        Returns:
            Self
        """
        city_key=f"weather_data:{self.city}"
        self.r.json().set(city_key, '.', json.dumps(self.weather_data))
        return self
