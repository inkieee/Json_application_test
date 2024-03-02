import json
import matplotlib.pyplot as plt
import numpy as np

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
        # Initialize lists to store data
        latitudes = []
        longitudes = []
        temperatures = []
        city_names = []

        # Process the retrieved keys
        for city_key in city_keys:
            
            # Get City Data from Redis
            json_data = self.r.json().get(city_key) #coded raw json
            data = json.loads(json_data) #decoded json

            coordinates = data['coord']
            lat = coordinates['lat']
            lon = coordinates['lon']
            
            main=data['main']
            temperature=main['temp']

            name = data['name']

            # Append data to lists
            latitudes.append(lat)
            longitudes.append(lon)
            temperatures.append(temperature)
            city_names.append(name)

        # Latitude vs Temperature
        plt.figure(figsize=(8, 5))
        for i, city_name in enumerate(city_names):
            plt.scatter(latitudes[i], temperatures[i], label=city_name, s=40, c=plt.cm.viridis(i / len(city_names)))  # Use colormap
        plt.xlabel("Latitude")
        plt.ylabel("Temperature (Fahrenheit)")
        plt.title("Temperature by Latitude")
        plt.grid(True)
        plt.xticks(np.arange(-90, 90, 10))
        plt.legend(loc="upper left", bbox_to_anchor=(1.02, 1))
        plt.show()

        # Longitude vs Temperature
        plt.figure(figsize=(8, 5))
        for i, city_name in enumerate(city_names):
            plt.scatter(longitudes[i], temperatures[i], label=city_name, s=40, c=plt.cm.viridis(i / len(city_names)))  # Use colormap
        plt.xlabel("Longitude")
        plt.ylabel("Temperature (Fahrenheit)")
        plt.title("Temperature by Longitude")
        plt.grid(True)
        plt.xticks(np.arange(-180, 180, 10))
        plt.legend(loc="upper left", bbox_to_anchor=(1.02, 1))
        plt.show()


