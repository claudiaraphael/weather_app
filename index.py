import requests

API_KEY = "668b1bdb2090da8f8d244325f4e729a6" # test key
API_URL = "http://api.openweathermap.org/data/2.5/forecast"

# Example API call:
# http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={API key}

city = input("Enter the name of the city: ")

API_CALL = f"{API_URL}?q={city}&appid={API_KEY}"

### Make the API call
response = requests.get(API_CALL)

# Check if the API call was successful (status code 200)
if response.status_code == 200:
    data = response.json()
    print("API call successful!")
