import requests

API_KEY = "668b1bdb2090da8f8d244325f4e729a6" # test key
API_URL = "https://dashboard.openweather.co.uk/home"

city = input("Enter the name of the city: ")
request_url = f"{API_URL}?q={city}&appid={API_KEY}"