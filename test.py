import requests as r
from bs4 import BeautifulSoup

headers = {
        'User-Agent': 'WebIR Crawler',
        'From': 'Kasetsart University'
        }

a = r.get("https://www.metacritic.com/game/xbox-one/red-dead-redemption-2/", headers=headers)
critic = r.get("https://www.metacritic.com/game/xbox-one/red-dead-redemption-2/critic-reviews", headers=headers)

# f = open("test.html", "w")
# f.write(a.text)
# f.close()

f = open("critic.html", "w")
f.write(critic.text)
f.close()

f = open("test.html", "r")
a = f.read()
f.close()

f = open("critic.html", "r")
critic = f.read()
f.close()

'''
soup = BeautifulSoup(a, "html.parser")

name = soup.find("a", {"class" : ["hover_none"]})
name = name.find("h1").string.strip()
print(name)

platform = soup.find("span", {"class" : ["platform"]})
platform = platform.find("a").string.strip()
print(platform)

genre = soup.find("li", {"class" : ["summary_detail product_genre"]})
children = genre.findChildren("span" , class_= "data",recursive=False)
list_genre = []
for child in children:
        #print(child.string.strip())
        list_genre.append(child.string.strip())
print(list_genre)

dev = soup.find("li", {"class" : ["summary_detail developer"]})
dev = dev.find("span", {"class" : "data"}).string.strip()
print(dev)

summary = soup.find("span", {"class" : ["blurb blurb_expanded"]})
summary = summary.string.strip()
print(summary)

'''
data = {}
'''
data["Name"] = name
data["Platform"] = platform
data["Genre"] = list_genre
data["Developer"] = dev
data["Summary"] = summary
'''
data["Review"] = {}

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