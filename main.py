import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.com/gp/product/B07J4SXNQ5/ref=ox_sc_saved_title_4?smid=ATVPDKIKX0DER&psc=1"

headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())
