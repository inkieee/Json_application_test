import json


class PlotCityWeather:
    """
    Class to plot weather data for cities in Redis
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
    
    def plot_city_weather(self, city_keys):
        # Process the retrieved keys
        for city_key in city_keys:
            print(city_key)
            json_data = self.r.json().get(city_key) #coded raw json
            data = json.loads(json_data) #decoded json
            print(data)

            # timezone = data['timezone']
            coordinates = data['coord']
            lat = coordinates['lat']
            lon = coordinates['lon']

            main=data['main']
            temperature=main['temp']

            # print(f"Timezone: {timezone}")
            print(f"Coordinates: {coordinates}")
            print(f"Lat/Long: {lat},{lon}")
            print(f"Temperature: {temperature}")
    