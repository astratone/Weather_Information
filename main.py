import requests
from pprint import pprint

API_Key = ''  # Insert your API key

city = input("Enter a city: ")

base_url = "http://api.openweathermap.org/data/2.5/forecast?appid="+API_Key+"&q="+city

weather_data = requests.get(base_url).json()

pprint(weather_data)
