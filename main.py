

# obtain api

# obtain cities to do something with
# read from file maybe

# put cities into memory

# instantiate a api object to store api data
# for city in list
#   city_data = object_that_instantiation_results_in_call_to_obtain_data, and puts into redis
#       //so this object is;
#       //  get api data for city
#       //  put that data into redis
#       //  destroy object
#   // now you have a lot of objects with data per city
#   //does it make sense to put this data into objects here?
#   //for what?, maybe make objects in redis

# for city_object in objects in redis
#   do some outputs
#       1. plot city, temperature
#       2. maybe geolocation with redis?
#       2b. Aggregate average temperature over all cities between lat/long
#       2c. Search for cities with weather data b/w x and y
#       3. calculate tempeartures in varying scales

#from api_key_provider import ApiKeyProvider
#from weather_client import WeatherClient

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
        for city in self.cities:
            weather_data = self.weather_client.get_weather(city)
            if weather_data:
                # Process the weather data
                print(f"Weather data for {city}:")
                # (Extract and display relevant information from the data dictionary)
                # ...
            else:
                print(f"Failed to retrieve weather data for {city}.")

# Check if the script is run directly (not imported as a module)
if __name__ == "__main__":
    # Create WeatherApp instance (optional)
    weather_app = WeatherApp()

    # Add cities to the list (modify this section)
    weather_app.add_city("New York")
    weather_app.add_city("London")
    weather_app.add_city("Paris")

    # Run the app
    weather_app.run()
