import requests

class WeatherClient:
  """
  Class to interact with the OpenWeatherMap API.
  """
  def __init__(self, api_key_provider):
    """
    Initializes the client with an ApiKeyProvider object.

    Args:
        api_key_provider (ApiKeyProvider): An object providing the API key.
    """
    self.api_key_provider = api_key_provider

  def get_weather(self, city_name):
    """
    Retrieves weather data for a given city.

    Args:
        city_name (str): Name of the city to get weather data for.

    Returns:
        dict: Dictionary containing the weather data or None if there's an error.
    """
    api_key = self.api_key_provider.get_api_key()
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&exclude=hourly,daily&units=imperial&appid={api_key}"
    # url = f"https://api.openweathermap.org/data/3.0/onecall?q={city_name}&appid={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
      return response.json()
    else:
      print(f"Error: {response.status_code}")
      return None

