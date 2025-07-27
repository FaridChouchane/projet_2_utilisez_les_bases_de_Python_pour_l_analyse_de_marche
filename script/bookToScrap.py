#######################################
##                                   ##
##           Librairies              ##
##                                   ##
#######################################

from bs4 import BeautifulSoup
import requests
from pprint import pprint
import csv


#######################################
##                                   ##
##                URL                ##
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

with open("scrapped_books.csv", 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = [
        'universal_product_code (upc)',
        'title',
        'price_including_tax',
        'price_excluding_tax',
        'number_available',
        'product_description',
        'category',
        'review_rating',
        'image_url'
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()

#######################################
##                                   ##
##   RECUPERATION  product_page_url  ##
##                                   ##
#######################################   
print("")
print("#" * 20, "URLs des livres", "#" * 20)
print("")

urls = []

for i in soup.find_all("h3"):
    a = i.find('a')
    urls.append(URL + a['href'])

for url in urls:    
    print(url)

print("")
print("#" * 20, "          ", "#" * 20)
print("")
#######################################
##                                   ##
##     RECUPERATION                  ##
##     universal_product_code (upc)  ##
##                                   ##
#######################################

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
