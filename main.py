# Name: Edward Tomczak @EdwardT97
#
# Created: 10/08/2019 2:54 PM CST
# Updated: 10/09/2019 9:04 AM CST
#
# Program Description: Scans directed amazon URLs for deals and returns
# price analytics for specified products.

import requests
from bs4 import BeautifulSoup
import smtplib
import re

URL = "https://www.amazon.com/gp/product/B07598SX6S/ref=ox_sc_saved_title_7?smid=ATVPDKIKX0DER&psc=1"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
    "like Gecko) Chrome/77.0.3865.90 Safari/537.36"}


def check_price():

    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

    title = soup2.find(id="productTitle").get_text()

    price = soup2.find(id="priceblock_ourprice").get_text()
    fixed_price = re.sub('[^a-zA-Z0-9 \n\.]', '', price)
    converted_price = float(fixed_price[0:5])

    if converted_price < 0.200:
        send_mail()

    print(converted_price)
    print(title.strip())

    if converted_price < 0.200:
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('username@gmail.com', '**********')

    subject = 'Price fell down!'
    body = 'Check the amazon link: ' \
           'https://www.amazon.com/gp/product/B07598SX6S/ref=ox_sc_saved_title_7?smid=ATVPDKIKX0DER&psc=1'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'sendingusername@gmail.com',
        'receivingusername@gmail.com',
        msg
    )
    print('EMAIL HAS BEEN SENT')

    server.quit()


check_price()
