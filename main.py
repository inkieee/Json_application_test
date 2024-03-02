
#from module, import class
from ApiKeyProvider import ApiKeyProvider
from WeatherClient import WeatherClient
from InsertRedisData import InsertRedisData
from PlotCityWeather import PlotCityWeather
from SortCityTemp import SortCityTemp
from FindCitiesBelowAvgTemp import FindCitiesBelowAvgTemp

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
        # r.flushall()


        # Insert Weather Data into Redis
        #########################################
        # Commented for now to save on API calls
        #########################################
        # for city in self.cities:
        #     weather_data = self.weather_client.get_weather(city)
        #     if weather_data:
        #         # print(f"\nCity: ",city)
        #         # print(weather_data)
        #         InsertRedisData(city, weather_data, r).insert_weather_data()
        #     else:
        #         print(f"Failed to retrieve weather data for {city}.")

        # Do processing with data
        # #Processing 1 object: Plot
        # city_plotter = PlotCityWeather(r)
        # city_keys = city_plotter.get_city_keys()
        # city_plotter.plot_city_weather(city_keys)

        # #Processing 2 object: Sort city by temp
        # city_sorter = SortCityTemp(r)
        # city_keys = city_sorter.get_city_keys()
        # sorted_cities, sorted_temperatures = city_sorter.sort_city_temp(city_keys)

        # print("Cities and temperatures sorted by temperature (ascending):")
        # for i, city in enumerate(sorted_cities):
        #     # Find the maximum length of (city names + ':') for consistent formatting
        #     max_city_length = max(len(city) + 1 for city in sorted_cities)  # Add 1 for the colon

        #     # Pad the city name and colon with spaces to ensure alignment
        #     formatted_city_colon = f"{city}:"
        #     padded_city = formatted_city_colon.ljust(max_city_length)

        #     # Format temperature with two decimal places (even for zero)
        #     formatted_temperature = f"{sorted_temperatures[i]:.2f}"  

        #     # Concatenate the padded city name and formatted temperature
        #     formatted_output = f"{padded_city} {formatted_temperature}"

        #     print(formatted_output)

        #Processing 3 object
        #Find cities with temps above average
        find_cities = FindCitiesBelowAvgTemp(r)
        city_keys = find_cities.get_city_keys()
        city_data, avg_temp = find_cities.get_city_temperatures(city_keys)
        cities_below_avg = find_cities.find_cities_below_avg(city_data, avg_temp)

        if cities_below_avg:
            print(f"Average temp: {avg_temp:.2f}")
            print("Cities with temperatures below average:")
            for city in cities_below_avg:
                print(f"\t{city}")
        else:
            print("No cities found with temperatures below the average.")

# Check if the script is run directly (not imported as a module)
if __name__ == "__main__":
    # Create WeatherApp instance (optional)
    weather_app = WeatherApp()

    # Add cities to the list
    weather_app.add_city("New York City")
    weather_app.add_city("London")
    weather_app.add_city("Paris")
    weather_app.add_city("Tokyo")
    weather_app.add_city("Shanghai")
    weather_app.add_city("Taipei")
    weather_app.add_city("Sydney")
    weather_app.add_city("Moscow")
    weather_app.add_city("Beijing")
    weather_app.add_city("Berlin")
    weather_app.add_city("Taizhong")
    weather_app.add_city("Mount Laurel")
    weather_app.add_city("Cherry Hill")
    weather_app.add_city("New Delhi")
    weather_app.add_city("Cairo")
    weather_app.add_city("Ottawa")
    weather_app.add_city("Canberra")
    weather_app.add_city("Buenos Aires")
    weather_app.add_city("Seoul")
    weather_app.add_city("Tehran")
    weather_app.add_city("Mexico City")
    weather_app.add_city("Riyadh")
    weather_app.add_city("Madrid")
    weather_app.add_city("Bangkok")
    weather_app.add_city("Amsterdam")

    # Run the app
    weather_app.run()
