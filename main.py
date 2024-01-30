import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "85c79069e246983359a87f17c03419b0"


weather_params = {
    "lat" : 41.492901,
    "lon" : 13.830570,
    "cnt" : 4,
    "appid" : api_key

}
response = requests.get(f"{OWM_Endpoint}", params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data)

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    print("Bring an umbrella")