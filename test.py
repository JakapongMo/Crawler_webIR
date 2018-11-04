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


#dev = soup.find("li", {"class" : ["summary_detail developer"]})
#print(dev.find("span", {"class" : "data"}).string.strip())

genre = soup.find("li", {"class" : ["summary_detail product_genre"]})
children = genre.findChildren("span" , class_= "data",recursive=False)
list_genre = []
for child in children:
        print(child.string.strip())
        list_genre.append(child.string.strip())
print(list_genre)



data = {}
data["Name"] = ""
data["Platform"] = ""
data["Genre"] = ""
#data["Developer"] = dev
data["Summary"] = ""
data["Review"] = {}

f = open("dict.json", "w")
f.write(str(data))
f.close()