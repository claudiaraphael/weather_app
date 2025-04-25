import requests

API_KEY = "your_api_key_here"
API_URL = "https://api.example.com/data"

city = input("Enter the name of the city: ")
request_url = f"{API_URL}?q={city}&appid={API_KEY}"