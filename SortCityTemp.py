import json

class SortCityTemp:
    """
    Class to sort weather data for cities in Redis
    """
    def __init__(self, r):
        """
        Initializes object to pass in weather data 

        Args:
            r: Redis connection object
        """
        self.r = r

    def get_city_keys(self):
        # Pattern to match keys starting with "weather_data:"
        pattern = "weather_data:*"

        # Get all keys matching the pattern
        keys = self.r.keys(pattern)

        return keys
    
    def sort_city_temp(self, city_keys):
        """
        Sorts city names by temperature.

        Args:
            city_keys: List of city keys to sort.

        Returns:
            list: A list of city names sorted by temperature in ascending order.
        """

        city_data = {}  # Dictionary to store city name and temperature pairs
        for city_key in city_keys:
            json_data = self.r.json().get(city_key)
            data = json.loads(json_data)

            main = data['main']
            temperature = main['temp']
            name = data['name']
            city_data[name] = temperature

        # Sort cities by temperature in ascending order
        sorted_cities = sorted(city_data, key=city_data.get)
        sorted_temperatures = [city_data[city] for city in sorted_cities]

        return sorted_cities, sorted_temperatures
