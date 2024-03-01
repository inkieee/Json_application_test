import json
import matplotlib.pyplot as plt

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

        # Create scatter plot with different colors and labels
        plt.figure(figsize=(8, 5))
        for i, city_name in enumerate(city_names):
            plt.scatter(latitudes[i], longitudes[i], label=city_name, s=80, c=plt.cm.viridis(i/len(city_names)))  # Use colormap

        # Add plot elements
        plt.xlabel("Latitude")
        plt.ylabel("Longitude")
        plt.title("Temperature by City Location")
        plt.legend()
        plt.grid(True)

        # Show the plot
        plt.show()

    