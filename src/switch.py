import requests
from bs4 import BeautifulSoup

URL = "http://192.168.101.251"
page = requests.get(URL)

print(page.text)
soup = BeautifulSoup(page.content, "html.parser")
