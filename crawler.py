import requests as r
from bs4 import BeautifulSoup
import Filterer as ftr

headers = {
        'User-Agent': 'WebIR Crawler',
        'From': 'Kasetsart University'
        }

a = r.get("https://www.metacritic.com/game/xbox-one/red-dead-redemption-2/", headers=headers)
critic = r.get("https://www.metacritic.com/game/xbox-one/red-dead-redemption-2/critic-reviews")

soup = BeautifulSoup(a.text, "html.parser")

name = ftr.extract_name(soup)
platform = ftr.extract_platform(soup)
dev = ftr.extract_developer(soup)
summary = ftr.extract_summary(soup)

print(name)
print(platform)
print(dev)
print(summary)

data = {}
data["Name"] = name
data["Platform"] = platform
data["Genre"] = ""
data["Developer"] = dev
data["Summary"] = summary
data["Review"] = {}

f = open("dict.json", "w")
f.write(str(data))
f.close()