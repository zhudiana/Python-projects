
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.python.org/events/")

event_title = driver.find_elements(By.CLASS_NAME, value="event-title")
event_date = driver.find_elements(By.TAG_NAME, value="time")

my_events = {}

for i in range(len(event_date)):
    my_events[i]={
        "time": event_date[i].text,
        "name": event_title[i].text
    }

print(my_events)

time.sleep(10)
driver.quit()