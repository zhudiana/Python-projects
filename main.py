from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time



ZILLOW = "https://appbrewery.github.io/Zillow-Clone/"
FORM = "https://docs.google.com/forms/d/e/1FAIpQLSdEQm3WE3zGC6McFBlBO-YqIMhh_Yl0sRI6QkilJE0RVfm6GQ/viewform?usp=sf_link"

response = requests.get(ZILLOW)
soup = BeautifulSoup(response.text, 'html.parser')

all_prices = soup.select(".PropertyCardWrapper span")
all_links = soup.select(".StyledPropertyCardDataWrapper a")
all_address = soup.select(".StyledPropertyCardDataWrapper address")

all_prices = [price.get_text().replace("/mo", "").split("+")[0] for price in all_prices if "$" in price.text]
all_links = [link["href"] for link in all_links]
all_addresses = [address.get_text().replace(" | ", " ").strip() for address in all_address]

#Selenium
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


for n in range(len(all_links)):
    driver.get(FORM)
    time.sleep(2)

    address = driver.find_element(by=By.XPATH,
                                  value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(by=By.XPATH,
                                value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(by=By.XPATH,
                               value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(by=By.XPATH,
                                        value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

    address.send_keys(all_addresses[n])
    price.send_keys(all_prices[n])
    link.send_keys(all_links[n])
    submit_button.click()