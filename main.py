import requests
from bs4 import BeautifulSoup
import smtplib
import time

EMAIL = "--"
PASSWORD = "--"

response=requests.get(
    "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1",
    headers={"Accept-Language":"en-US,en;q=0.5","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0" })
amazon_html = response.text

soup = BeautifulSoup(amazon_html, "lxml")

price = soup.find(class_="aok-offscreen").getText()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)


product_name = soup.find(id="productTitle").getText().strip()



if price_as_float < 100:
    message = f"{product_name} is now {price_as_float}"

    with smtplib.SMTP(YOUR_SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )