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

      city_key=f"weather_data:{city}"
      r.json().set(city_key, '.', json.dumps(weather_data))
