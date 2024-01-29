import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "85c79069e246983359a87f17c03419b0"


weather_params = {
    "lat" : 41.492901,
    "lon" : 13.830570,
    "appid" : api_key

}
response = requests.get(f"{OWM_Endpoint}", params=weather_params)
data = response.json()
print(data)