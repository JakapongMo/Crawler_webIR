import os
import requests as r
from urllib.parse import urljoin
from bs4 import BeautifulSoup

headers = {
        'User-Agent': 'WebIR Crawler',
        'From': 'Kasetsart University'
        }

root_url = "https://www.metacritic.com"
urls = []
for i in range(157):
    print("Page : ", i)
    try:
        search_url = "https://www.metacritic.com/browse/games/score/metascore/all/all/filtered?sort=desc&page=" + str(i)
        html = r.get(search_url, headers=headers)
        soup = BeautifulSoup(html.text, "html.parser")
        ol = soup.find("ol", {"class" : "list_products list_product_condensed"})
        for url in ol.find_all('a'):
            relative_url = url.get('href')
            absolute_url = root_url + relative_url
            urls.append(absolute_url)
    except:
        print("Error!!!")


with open("urls.txt", "w") as f:
    for url in urls:
        f.write(url + "\n")
