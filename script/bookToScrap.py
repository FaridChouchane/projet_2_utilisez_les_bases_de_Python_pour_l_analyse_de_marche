#######################################
##                                   ##
##           Librairies              ##
##                                   ##
#######################################

from bs4 import BeautifulSoup
import requests
from pprint import pprint

#######################################
##                                   ##
##           URL                     ##
##                                   ##
#######################################

URL = "https://books.toscrape.com/"

response = requests.get(URL)

print(f"status code : {response.status_code}")

soup = BeautifulSoup(response.text, "html.parser")
pprint(soup.prettify())

with open("book.html", "w", encoding = "utf-8") as book:
    book.write(soup.prettify())
