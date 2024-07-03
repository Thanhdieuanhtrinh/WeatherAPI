from dotenv import load_dotenv
import os
import sys

# Load the environment variables from .env file
load_dotenv('.env')

# Get the API key from the environment variable
# api_key = os.getenv('OpenWeatherMapAPIKey')
# print(api_key) 
api_key ="3fd85c34a7e73424a6ce64098d0dc87b"

# Import the requests library
import requests

location = input("Nhap ten thanh pho: ")
response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=5&appid={api_key}")

# print(response.status_code)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Extract the weather data from the response
    geo_data = response.json()
    # print(geo_data)
    if len(geo_data) ==0:
        print("k tim thay vi tri")
        sys.exit()

else:
    print("Error: Failed to retrieve location data")

lat = geo_data[0]["lat"]
lon = geo_data[0]["lon"]
# print(lat,lon)

import requests


# Define the API endpoint URL
response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric&lang=vi")


# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Extract the weather data from the response
    weather_data = response.json()
    # print(weather_data)
else:
    print("Error: Failed to retrieve weather data")

print(f"""Tinh hinh thoi tiet {weather_data["weather"][0]["description"]}
Nhiet do la {weather_data["main"]["temp"]} 
Tam nhin xa {weather_data["visibility"]/1000} km""")