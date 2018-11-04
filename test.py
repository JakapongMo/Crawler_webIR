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

a = r.get("https://www.metacritic.com/game/xbox-one/red-dead-redemption-2/", headers=headers)
critic = r.get("https://www.metacritic.com/game/xbox-one/red-dead-redemption-2/critic-reviews", headers=headers)

soup = BeautifulSoup(a, "html.parser")

genre = soup.find("li", {"class" : ["summary_detail product_genre"]})
children = genre.findChildren("span" , class_= "data",recursive=False)
list_genre = []
for child in children:
        #print(child.string.strip())
        list_genre.append(child.string.strip())
print(list_genre)


#print (critic)
soup_critic = BeautifulSoup(critic, "html.parser")



first_review = soup_critic.find("li", {"class" : ["review critic_review first_review"]})
#print (first_review)
text = first_review.find("div", {"class" : "review_body"}).string.strip()
score = first_review.find("div", {"class" : "metascore_w"}).string.strip()
source = first_review.find("div", {"class" : "source"}).string.strip()
link = first_review.find("a", {"class" : "external"}, href=True)['href']
print (text)
print (score)
print (source)
print (link)
a = r.get(link, headers=headers)
print (a.status_code)
print ("=============================")
reviews = soup_critic.find_all("li", {"class" : ["review critic_review"]})
#first_review = review.findChildren("li" , class_= "review critic_review first_review",recursive=False)

print (len(reviews))



for review in reviews:
        text = review.find("div", {"class" : "review_body"}).string.strip()
        score = review.find("div", {"class" : "metascore_w"}).string.strip()
        source = review.find("div", {"class" : "source"}).string.strip()
        link = review.find("a", {"class" : "external"}, href=True)['href']
        print (text)
        print (score)
        print (source)
        print (link)
        a = r.get(link, headers=headers)
        print (a.status_code)
        print ("=============================")
#print (len(reviews))



last_review = soup_critic.find("li", {"class" : ["review critic_review last_review"]})
#print (last_review)
text = last_review.find("div", {"class" : "review_body"}).string.strip()
score = last_review.find("div", {"class" : "metascore_w"}).string.strip()
source = last_review.find("div", {"class" : "source"}).string.strip()
link = last_review.find("a", {"class" : "external"}, href=True)['href']
print (text)
print (score)
print (source)
print (link)
a = r.get(link, headers=headers)
print (a.status_code)
print ("=============================")
f = open("dict.json", "w")
f.write(str(data))
f.close()