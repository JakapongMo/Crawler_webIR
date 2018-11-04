def extract_name(soup):
    name = soup.find("a", {"class" : ["hover_none"]})
    name = name.find("h1").string.strip()
    return name

def extract_platform(soup):
    platform = soup.find("span", {"class" : ["platform"]})
    platform = platform.find("a").string.strip()
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
    return ""

def extract_review(soup):
    return ""

def extract_source(soup):
    return ""

def extract_url(soup):
    return ""

def extract_metascore(soup):
    score = soup.find("span", {"itemprop" : ["ratingValue"]})
    score = score.string.strip()
    return score