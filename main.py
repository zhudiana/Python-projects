import requests
from datetime import datetime

USER_NAME = "yodit"
TOKEN = "kdfemknfsnsfdfnksnff"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"


user_params = {
    "token" : TOKEN,
    "username" : USER_NAME,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

pixel_creation_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today?")
}


response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

updated_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity":"35"
}
# response = requests.put(url=updated_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"


# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
