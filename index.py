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
    # The response will be in JSON format, so you can parse it using the json() method
    # and access the data you need.
    # For example, to get the weather description for the first forecast in the list:
    data = response.json()
    print("API call successful!")
    #print(f"Status code: {response.status_code}")
    #print(f"Response: {response.text}")

    weather = data['list'][0]['weather'][0]['description']
    temperature = data['list'][0]['main']['temp'] - 273.15  # Convert from Kelvin to Celsius
    print(weather)
    print(f"Temperature: {temperature:.2f} °C")
else:
    print("API call failed!")
    print(f"Status code: {response.status_code}")
    print(f"Response: {response.text}")
            
  
# Error handling

# Print the full API response to see what went wrong
# print("API response:", data)

# Safely try to get weather info
#if 'weather' in data['list'][0]:
    # Acessa a descrição do clima na primeira previsão da lista
#    weather = data['list'][0]['weather'][0]['description']
#    print("Weather description:", weather)

# elif 'wheather' in data['list'][0]:
#    print("❌ wheather key is in data somewhere else.", data)

# else:
#    print("❌ wheather key not found in data.", data)