import requests as r
from bs4 import BeautifulSoup

headers = {
        'User-Agent': 'haha',
        'From': 'haha'
        }

a = r.get("https://www.metacritic.com/game/xbox-one/red-dead-redemption-2/", headers=headers)

# f = open("test.html", "w")
# f.write(a.text)
# f.close()

f = open("test.html", "r")
a = f.read()
f.close()
#print(a)

soup = BeautifulSoup(a, "html.parser")

name = soup.find("a", {"class" : ["hover_none"]})
print(name.string.strip())

dev = soup.find("li", {"class" : ["summary_detail developer"]})
print(dev.find("span", {"class" : "data"}).string.strip())

data = {}
data["Name"] = ""
data["Platform"] = ""
data["Genre"] = ""
data["Developer"] = dev
data["Summary"] = ""
data["Review"] = {}

f = open("dict.json", "w")
f.write(str(data))
f.close()