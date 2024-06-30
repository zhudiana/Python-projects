from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

ACCOUNT_EMAIL = 'YOUR EMAIL'
ACCOUNT_PASSWORD = 'YOUR PASSWORD'

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.linkedin.com/jobs/collections/recommended/?currentJobId=3961525098&discover=recommended&discoveryOrigin=JOBS_HOME_JYMBII")

user_name = driver.find_element(By.ID, value="username")
user_name.send_keys(ACCOUNT_EMAIL)
password = driver.find_element(By.ID, value="password")
password.send_keys(ACCOUNT_PASSWORD)
password.send_keys(Keys.ENTER)

easy_apply = driver.find_element(By.CLASS_NAME, value="jobs-apply-button")
easy_apply.click()

submit = driver.find_element(By.XPATH, '//button[contains(@aria-label, "Submit application") and .//span[text()="Submit application"]]')
submit.click()

time.sleep(100)
driver.quit()