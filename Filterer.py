def extract_name(soup):
    name = soup.find("a", {"class" : ["hover_none"]})
    name = name.find("h1").string.strip()
    return name

def extract_platform(soup):
    platform = soup.find("span", {"class" : ["platform"]})
    if platform.find("a"):
        platform = platform.find("a").string.strip()
    else:
        platform = platform.string.strip()
    return platform

def extract_developer(soup):
    dev = soup.find("li", {"class" : ["summary_detail developer"]})
    dev = dev.find("span", {"class" : "data"}).string.strip()
    return dev

def extract_summary(soup):
    summary = soup.find("span", {"class" : ["blurb blurb_expanded"]})
    summary = summary.string.strip()
    return summary

def extract_genre(soup):
    genre = soup.find("li", {"class" : ["summary_detail product_genre"]})
    children = genre.findChildren("span" , class_= "data",recursive=False)
    list_genre = []
    for child in children:
        list_genre.append(child.string.strip())
    return list_genre

def extract_review_dicts(soup_critic):
    list_of_review_dicts = []
    first_review = soup_critic.find("li", {"class" : ["review critic_review first_review"]})
    text = first_review.find("div", {"class" : "review_body"}).string.strip()
    try:
        score = first_review.find("div", {"class" : "metascore_w"}).string.strip()
    except AttributeError:
        score = -1
    source = first_review.find("div", {"class" : "source"}).string.strip()
    try:
        link = first_review.find("a", {"class" : "external"}, href=True)['href']
    except TypeError:
        link = "no_link"
    review_dict = {}
    review_dict['text'] = text
    review_dict['source'] = source
    review_dict['score_review'] = score
    review_dict['url_source'] = link

    list_of_review_dicts.append(review_dict)
    
    
    reviews = soup_critic.find_all("li", {"class" : ["review critic_review"]})
    for review in reviews:
        review_dict = {}
        text = review.find("div", {"class" : "review_body"}).string.strip()
        print (text)
        try:
            score = review.find("div", {"class" : "metascore_w"}).string.strip()
        except AttributeError:
            score = -1
        print(score)
        source = review.find("div", {"class" : "source"}).string.strip()
        print (source)
        try:
            link = review.find("a", {"class" : "external"}, href=True)['href']
        except TypeError:
            link = "no_link"
        print (link)
        review_dict['text'] = text
        review_dict['source'] = source
        review_dict['score_review'] = score
        review_dict['url_source'] = link
        list_of_review_dicts.append(review_dict)

    review_dict = {}
    last_review = soup_critic.find("li", {"class" : ["review critic_review last_review"]})
    text = last_review.find("div", {"class" : "review_body"}).string.strip()
    try:
        score = last_review.find("div", {"class" : "metascore_w"}).string.strip()
    except AttributeError:
        score = -1
    source = last_review.find("div", {"class" : "source"}).string.strip()
    try:
        link = last_review.find("a", {"class" : "external"}, href=True)['href']
    except TypeError:
        link = "no_link"
    review_dict['text'] = text
    review_dict['source'] = source
    review_dict['score_review'] = score
    review_dict['url_source'] = link
    list_of_review_dicts.append(review_dict)
    return list_of_review_dicts

def extract_metascore(soup):
    score = soup.find("span", {"itemprop" : ["ratingValue"]})
    score = score.string.strip()
    return score
