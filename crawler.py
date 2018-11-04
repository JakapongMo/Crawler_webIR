import requests
from bs4 import BeautifulSoup
import Filterer as ftr
import time

headers = {
        'User-Agent': 'WebIR Crawler',
        'From': 'Kasetsart University'
        }

error_url = []
count_pass = 0
count_error = 0
count_all = 0

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
        r = requests.get(url, headers=headers, timeout=5)
        text = r.text
        status = r.status_code
    except(KeyboardInterrupt, SystemExit):
        raise
    except:
        print('GET PAGE ERROR!')
        error_url.append(url)
    return text, status

with open("j.txt", "r") as f:
    urls = eval(f.read())

results = []
for url in urls:
    url = url.strip()
    print("Url : " + url)
    critic_url = url + "/critic-reviews"
    try:
        detail, detail_status = get_page(url)
        critic, critic_status = get_page(critic_url)

        if detail_status == 200 and critic_status == 200:
            detail = BeautifulSoup(detail, "html.parser")

            name = ftr.extract_name(detail)
            platform = ftr.extract_platform(detail)
            dev = ftr.extract_developer(detail)
            summary = ftr.extract_summary(detail)
            genre = ftr.extract_genre(detail)
            metascore = ftr.extract_metascore(detail)

            soup_critic = BeautifulSoup(critic, "html.parser")
            list_of_review_dicts = ftr.extract_review_dicts(soup_critic)

            # print(name)
            # print(platform)
            # print(dev)
            # print(summary)
            # print(genre)
            # print(list_of_review_dicts)

            result = make_json(name, platform, genre, dev, summary, metascore, list_of_review_dicts)
            results += result

            with open("result.txt", "a", encoding="utf-8") as f:
                f.write(str(result))

            with open("error.txt", "w") as f:
                f.write(str(error_url))

            count_pass += 1
        count_all += 1
        with open("count.txt", "w") as f:
            f.writelines(str(count_pass) + "\n")
            f.writelines(str(count_all))
    except(KeyboardInterrupt, SystemExit):
        raise
    except:
        error_url.append(url)
        with open("error.txt", "w") as f:
            f.write(str(error_url))

with open("results.txt", "w", encoding="utf-8") as f:
    f.write(str(results))