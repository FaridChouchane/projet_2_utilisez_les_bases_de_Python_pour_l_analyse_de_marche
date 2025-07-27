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


BASE_URL  = "https://books.toscrape.com/"
URL = BASE_URL 

urls = []


response = requests.get(URL)

# print(f"status code : {response.status_code}")

soup = BeautifulSoup(response.text, "html.parser")
# pprint(soup.prettify())

with open("book.html", "w", encoding = "utf-8") as book:
    book.write(soup.prettify())



#######################################
##                                   ##
##   RECUPERATION  product_page_url  ##
##                                   ##
#######################################   
# print("")
# print("#" * 20, "URLs des livres", "#" * 20)
# print("")


# for i in soup.find_all("h3"):
#     a = i.find('a')
#     urls.append(URL + a['href'])

# for url in urls:    
#     print(url)

# print("")
# print("#" * 20, "          ", "#" * 20)
# print("")
#######################################
##                                   ##
##   RECUPERATION  product_page_url  ##
##   pourchaque page du site         ##
#######################################   
while True:    
    print(f"Scraping : {URL}")
    
    for i in soup.find_all("h3"):
        a = i.find('a')
        urls.append(BASE_URL + a['href'].replace("../../..", ""))
        
    for url in urls:
        print(url)
        
    print("")
    print("")
    print("")
    # Vérifier si un bouton "next" existe
    next_button = soup.find("li", class_="next")
    if next_button:
        next_page = next_button.find("a")["href"]

    next_page_url = BASE_URL + next_page.replace("../../..", "")

    if next_button:
        next_page = next_button.find("a")["href"]
        
        if URL == BASE_URL:
            URL = BASE_URL + next_page
            print(URL)
        else:
            URL = URL.rsplit("/", 1)[0] + "/" + next_page
            print(URL)
            
        response = requests.get(URL)
        soup = BeautifulSoup(response.text, "html.parser")
    else:
        break

# Affichage final des URLs
print("\n#################### URLs des livres ####################")
for url in urls:
    print(url)
print("\n#################### FIN ####################")
print(f"Total : {len(urls)} livres")