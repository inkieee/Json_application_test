import requests

# Replace with your file path (if different)
api_key_file = "api_key.conf"

with open(api_key_file, "r") as file:
    # Read the entire file contents
    file_content = file.read()

# Extract the API key using string manipulation
api_key = file_content.split("=")[1].strip()

# City name (replace with the city you want)
city_name = "London"

# API endpoint URL with formatted parameters
url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

# Send GET request and get response
response = requests.get(url)

# Check for successful response
if response.status_code == 200:
    # Parse JSON response
    data = response.json()

    # Extract relevant data
    city = data["name"]
    temperature = data["main"]["temp"] - 273.15  # Convert Kelvin to Celsius
    weather_description = data["weather"][0]["description"]

    # Print retrieved information
    print(f"City: {city}")
    print(f"Temperature: {temperature:.2f} °C")
    print(f"Weather: {weather_description}")

else:
    print(f"Error: {response.status_code}")
