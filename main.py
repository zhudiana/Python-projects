import requests
import datetime
import os

GENDER = "female"
WEIGHT_KG = 62
HEIGHT_CM = 162
AGE = 24

END_POINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENDPOINT = os.environ["SHEET_ENDPOINT"]

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]

USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ['PASSWORD']

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
}

exercise_text = input("Tell me which exercise you did: ")

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(END_POINT, json=parameters, headers=headers)
result = response.json()

today = datetime.date.today().strftime("%d/%m/%Y")
current_time = datetime.datetime.now().strftime("%X")


for exercise in result["exercises"]:
    sheet_parameters = {
        "workout": {
            "date": today,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(SHEET_ENDPOINT, json=sheet_parameters, auth=(USERNAME, PASSWORD))
    sheet_result = sheet_response.text
    print(sheet_result)


