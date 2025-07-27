from bs4 import BeautifulSoup
import requests

BASE_URL = "https://books.toscrape.com/"
URL = BASE_URL
urls = []

# Première requête
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

while True:    
    print(f"Scraping : {URL}")
    
    # Récupération des livres de la page actuelle
    for i in soup.find_all("h3"):
        a = i.find('a')
        urls.append(BASE_URL + a['href'].replace("../../..", ""))

    # Vérifier si un bouton "next" existe
    next_button = soup.find("li", class_="next")
    if next_button:
        next_page = next_button.find("a")["href"]

        if URL == BASE_URL:
            URL = BASE_URL + "catalogue/" + next_page
        else:
            URL = URL.rsplit("/", 1)[0] + "/" + next_page

        # ✅ Mettre à jour soup avec la nouvelle URL
        response = requests.get(URL)
        soup = BeautifulSoup(response.text, "html.parser")

    else:
        break

# Affichage final
print("\n#################### URLs des livres ####################")
for url in urls:
    print(url)
print("\n#################### FIN ####################")
print(f"Total : {len(urls)} livres")
