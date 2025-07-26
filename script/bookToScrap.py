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

# print(f"status code : {response.status_code}")

soup = BeautifulSoup(response.text, "html.parser")
# pprint(soup.prettify())

with open("book.html", "w", encoding = "utf-8") as book:
    book.write(soup.prettify())
    
#######################################
##                                   ##
##     CREATION FICHIER CSV          ##
##         A INCREMENTER             ##
##                                   ##
#######################################   


#  product_page_url

ppurl = soup.find_all("h3")

for p in ppurl:
    les_a = p.find_all('a')
    for a in les_a:
        for ppurl in a:
            url = URL + a['href']
            pprint(url)

# universal_product_code (upc)
print("")
print("#" * 20)
print("")

upcs = soup.find("th")

response = requests.get(url)
soup_upc = BeautifulSoup(response.text, "html.parser")
print("~" * 20)
print("~" * 20)
pprint(soup_upc.prettify())
print("~" * 20)
print("~" * 20)


for url in soup_upc:
    print(f"1 - {url}")
    

# for upc in upcs:
#     pprint(upc.text)
print("")
print("#" * 20)
print("")

# title
print("")
print("#" * 20)
print("")

title = soup.find_all("h3")

for p in title:
    les_a = p.find_all('a')
    for a in les_a:
        for title in a:
            pprint(f"- {a['title']}")

# price_including_tax
# price_excluding_tax
# number_available
# product_description
# category
# review_rating
# image_url
