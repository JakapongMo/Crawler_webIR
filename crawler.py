import requests
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
    return text.lower(), status

headers = {
        'User-Agent': 'WebIR Crawler',
        'From': 'Kasetsart University'
        }

with open("urls.txt", "r") as f:
    urls = f.readlines()

for url in urls:
    url = url.strip()
    critic_url = url + "/critic-reviews"

    detail = get_page(url)
    critic = get_page(critic_url)

    detail = BeautifulSoup(detail, "html.parser")

    name = ftr.extract_name(detail)
    platform = ftr.extract_platform(detail)
    dev = ftr.extract_developer(detail)
    summary = ftr.extract_summary(detail)
    genre = ftr.extract_genre(detail)

    critic = BeautifulSoup(critic, "html.parser")

    review = ftr.extract_review(critic)
    source = ftr.extract_source(critic)
    url = ftr.extract_url(critic)

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