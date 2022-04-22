import requests
from bs4 import BeautifulSoup
import smtplib
from re import sub
from decimal import Decimal

TARGET_PRICE = "TARGET PRICE"
ACCOUNT = "YOUR EMAIL"
PASSWORD = "YOUR PASSWORD"

URL = "https://www.amazon.com/MSI-Gaming-RTX-3080-Trio/dp/B095VZ6F73/ref=sr_1_16?crid=1Q9D2R1QS4201&keywords=" \
      "rtx+3080&qid=1649819639&s=electronics&sprefix=rtx+%2Celectronics%2C339&sr=1-16"

User_Agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " \
             "Chrome/100.0.4896.75 Safari/537.36"

Accept_Language = "en-US,en;q=0.9"

headers = {
    "Accept-Language": Accept_Language,
    "User-Agent": User_Agent
}

response = requests.get(URL, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

price_string = soup.find("span", class_="a-offscreen").getText()

float_price = float(Decimal(sub(r'[^\d.]', '', price_string)))

if float_price <= TARGET_PRICE:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=ACCOUNT,
                         password=PASSWORD)
        connection.sendmail(from_addr=ACCOUNT,
                            to_addrs=ACCOUNT,
                            msg=f"Subject: Amazon Price Alert!\n\nRTX 3080 Ti\nPrice: ${float_price}\nLink: {URL}")

