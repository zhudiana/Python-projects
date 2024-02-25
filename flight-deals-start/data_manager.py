import requests
from pprint import pprint


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get("https://api.sheety.co/7d6786c1b0ba602a6d97d02210c45ae7/flightDeals/prices")
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price":
                    {
                        "iataCode": city["iataCode"],
                    }
            }

            response = requests.put(
                url=f"https://api.sheety.co/7d6786c1b0ba602a6d97d02210c45ae7/flightDeals/prices/{city['id']}",
                json=new_data
            )
            print(response.text)
