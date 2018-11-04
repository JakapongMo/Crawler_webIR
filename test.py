import requests as r
from bs4 import BeautifulSoup
import Filterer as ftr

def make_json(name, platform, genre, developer, summary, review, source, url):
    data = {}
    data["Name"] = name
    data["Platform"] = platform
    data["Genre"] = ""
    data["Developer"] = dev
    data["Summary"] = summary
    data["Review"] = review
    data["Source"] = source
    data["Url"] = url
    return data

headers = {
        'User-Agent': 'WebIR Crawler',
        'From': 'Kasetsart University'
        }

a = r.get("https://www.metacritic.com/game/nintendo-64/the-legend-of-zelda-ocarina-of-time/", headers=headers)
critic = r.get("https://www.metacritic.com/game/nintendo-64/the-legend-of-zelda-ocarina-of-time/critic-reviews")

soup = BeautifulSoup(a.text, "html.parser")

score = soup.find("span", {"itemprop" : ["ratingValue"]})
score = score.string.strip()
print(score)
print("Metascore: ")

name = ftr.extract_name(soup)
platform = ftr.extract_platform(soup)
dev = ftr.extract_developer(soup)
summary = ftr.extract_summary(soup)
genre = ftr.extract_genre(soup)
review = ftr.extract_review(soup)
source = ftr.extract_source(soup)
url = ftr.extract_url(soup)

print(name)
print(platform)
print(dev)
print(summary)
print(genre)
print(review)
print(source)
print(url)

data = make_json(name, platform, genre, dev, summary, review, source, url)

f = open("dict.json", "w")
f.write(str(data))
f.close()