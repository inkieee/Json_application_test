#import pandas as pd
from db_config import get_redis_connection
import json

r = get_redis_connection()

## r.flushall()

data = {
   "lat":33.44,
   "lon":-94.04,
   "timezone":"America/Chicago",
   "timezone_offset":-18000,
   "current":{
      "dt":1684929490,
      "sunrise":1684926645,
      "sunset":1684977332,
      "temp":292.55,
      "feels_like":292.87,
      "pressure":1014,
      "humidity":89,
      "dew_point":290.69,
      "uvi":0.16,
      "clouds":53,
      "visibility":10000,
      "wind_speed":3.13,
      "wind_deg":93,
      "wind_gust":6.71,
      "weather":[
         {
            "id":803,
            "main":"Clouds",
            "description":"broken clouds",
            "icon":"04d"
         }
      ]
   }
}

city=input("Enter a city: ")
city_key=f"weather_data_{city}"

r.json().set(city_key, '.', json.dumps(data))

## This part is to retrieve the data

import redis
import json

# # Get JSON and decode 
json_data = r.json().get(city_key)
data = json.loads(json_data)

# Extract fields  
timezone = data['timezone']
lat = data['lat']
lon = data['lon']

print(f"Timezone: {timezone}")
print(f"Latitude: {lat}") 
print(f"Longitude: {lon}")