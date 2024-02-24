import requests
from pprint import pprint


class DataManager:
    response = requests.get("https://api.sheety.co/7d6786c1b0ba602a6d97d02210c45ae7/flightDeals/prices")
    sheet_data = response.json()["prices"]