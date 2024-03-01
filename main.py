
from ApiKeyProvider import ApiKeyProvider
from WeatherClient import WeatherClient
from InsertRedisData import InsertRedisData
from PlotCityWeather import PlotCityWeather

class WeatherApp:
    """
    Class to manage weather data retrieval for a list of cities.
    """
    def __init__(self, api_key_file="api_key.conf"):
        """
        Initializes the app with the API key file path.

        Args:
            api_key_file (str, optional): Path to the file containing the API key. Defaults to "api_key.conf".
        """
        self.api_key_provider = ApiKeyProvider(api_key_file)
        self.weather_client = WeatherClient(self.api_key_provider)
        self.cities = []  # Empty list to store city names

    def add_city(self, city_name):
        """
        Adds a city to the list of cities to retrieve weather data for.

        Args:
            city_name (str): Name of the city to add.
        """
        self.cities.append(city_name)

    def run(self):
        """
        Gets weather data for all cities in the list and displays the results.
        """
        # Open Redis Connection
        from db_config import get_redis_connection
        import json
        r = get_redis_connection()
        r.flushall()

        
        # Insert Weather Data into Redis
        for city in self.cities:
            weather_data = self.weather_client.get_weather(city)
            if weather_data:
                # print(f"\nCity: ",city)
                # print(weather_data)
                InsertRedisData(city, weather_data, r).insert_weather_data()
            else:
                print(f"Failed to retrieve weather data for {city}.")

        # Do processing with data
        #Processing 1 object: Plot
        city_plotter = PlotCityWeather(r)
        city_keys = city_plotter.get_city_keys()
        city_plotter.plot_city_weather(city_keys)

        #Processing 2 object

        #Processing 3 object
                

# Check if the script is run directly (not imported as a module)
if __name__ == "__main__":
    # Create WeatherApp instance (optional)
    weather_app = WeatherApp()

    # Add cities to the list
    weather_app.add_city("New York City")
    # weather_app.add_city("London")
    # weather_app.add_city("Paris")
    # weather_app.add_city("Tokyo")
    # weather_app.add_city("Shanghai")
    # weather_app.add_city("Taipei")
    # weather_app.add_city("Sydney")

    # Run the app
    weather_app.run()
