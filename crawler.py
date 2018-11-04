import requests
from bs4 import BeautifulSoup
import Filterer as ftr

headers = {
        'User-Agent': 'WebIR Crawler',
        'From': 'Kasetsart University'
        }

def make_json(name, platform, genre, developer, summary, metascore, list_of_review_dicts):
    result = []
    for review in list_of_review_dicts:
        data = {}
        data["Name"] = name
        data["Platform"] = platform
        data["Genre"] = genre
        data["Developer"] = dev
        data["Summary"] = summary
        data["Metascore"] = metascore
        data["Review"] = review["text"]
        data["Source"] = review["source"]
        data["Url"] = review["url_source"]
        data["Review_score"] = review["score_review"]
        result.append(data)
    return result

def get_page(url):
    global headers
    text = ""
    status = ""
    try:
        r = requests.get(url, headers=headers, timeout=2)
        text = r.text
        status = r.status_code
    except(KeyboardInterrupt, SystemExit):
        raise
    except:
        print('GET PAGE ERROR!')
    return text, status

with open("urls.txt", "r") as f:
    urls = f.readlines()

results = []
for url in urls:
    url = url.strip()
    print("Url : " + url)
    critic_url = url + "/critic-reviews"

    detail, detail_status = get_page(url)
    critic, critic_status = get_page(critic_url)

    if detail_status == 200 and critic_status == 200:
        detail = BeautifulSoup(detail, "html.parser")

        # name = ftr.extract_name(detail)
        # platform = ftr.extract_platform(detail)
        # dev = ftr.extract_developer(detail)
        # summary = ftr.extract_summary(detail)
        # genre = ftr.extract_genre(detail)
        # metascore = ftr.extract_metascore(detail)

        soup_critic = BeautifulSoup(critic, "html.parser")
        list_of_review_dicts = ftr.extract_review_dicts(soup_critic)

        # print(name)
        # print(platform)
        # print(dev)
        # print(summary)
        # print(genre)
        # print(list_of_review_dicts)

        #result = make_json(name, platform, genre, dev, summary, metascore, list_of_review_dicts)
        #results += result

        #with open("result.txt", "a") as f:
        #    f.write(str(result))

f = open("dict.json", "w")
f.write(str(results))
f.close()