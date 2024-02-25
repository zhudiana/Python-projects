import requests

FLIGHT_SEARCH_ENDPOINT = "https://api.tequila.kiwi.com/locations/query?term=PRG&locale=en-US&location_types=airport&limit=10&active_only=true"
API_KEY = "ImudNhmfUnCHamK-f6KTVVabDVMiyRIV"
# https://api.tequila.kiwi.com/locations/query?term=PRG&locale=en-US&location_types=airport&limit=10&active_only=true

class FlightSearch:
    def get_destination_code(self):
        response = requests.get(url=FLIGHT_SEARCH_ENDPOINT, headers=API_KEY)
        data = response.json()
        print(data)

flight_Search = FlightSearch()
flight_Search.get_destination_code()

