import json

class FindCitiesBelowAvgTemp:
    """
    Class to find cities with temperatures below the average of all cities.
    """

    def __init__(self, r):
        """
        Initializes object to pass in weather data.

        Args:
            r: Redis connection object.
        """
        self.r = r

    def get_city_keys(self):
        # Pattern to match keys starting with "weather_data:"
        pattern = "weather_data:*"

        # Get all keys matching the pattern
        keys = self.r.keys(pattern)

        return keys
    
    def get_city_temperatures(self, city_keys):
        """
        Gets city temperatures from Redis and calculates the average temperature.

        Returns:
            tuple: A tuple containing:
                - dict: A dictionary where keys are city names and values are temperatures.
                - float: The average temperature of all cities.
        """

        city_data = {}
        total_temp = 0

        for city_key in city_keys:
            try:                            
                json_data = self.r.json().get(city_key)
                data = json.loads(json_data)
                
                main = data["main"]
                temperature = main["temp"]
                name = data["name"]
                city_data[name] = temperature
                total_temp += temperature
            except KeyError:
                print(f"Error: Missing temperature data for key '{city_key}'")

        # Calculate average temperature (avoid division by zero)
        if len(city_data) > 0:
            avg_temp = total_temp / len(city_data)
        else:
            avg_temp = float("nan")  # Handle case with no city data

        return city_data, avg_temp

    def find_cities_below_avg(self, city_data, avg_temp):
        """
        Finds cities with temperatures below the average temperature.

        Args:
            city_data (dict): Dictionary containing city names and temperatures.
            avg_temp (float): Average temperature of all cities.

        Returns:
            list: A list of city names with temperatures below the average.
        """

        # city_data, avg_temp = self.get_city_temperatures()
        below_avg_cities = []

        for city, temperature in city_data.items():
            if temperature < avg_temp:
                below_avg_cities.append(city)

        return below_avg_cities

