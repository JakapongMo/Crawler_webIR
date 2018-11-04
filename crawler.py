import os
import requests
from urllib.parse import urljoin

# ดัก # / file ? : |
robot_path = "robots.txt"
save_path = "html/"

headers = {
        'User-Agent': '5810504639',
        'From': 'olan.s@ku.th'
        }

count = 0
frontier_q = ['http://www.ku.ac.th/web2012/']
# frontier_q = ['http://www.chem.sci.ku.ac.th']
visited_q = []
robots_list = []
sitemaps_list = []

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

def is_ku(url):
    return url.find(".ku.ac.th") != -1

def is_dynamic(url):
    return url.find("?") != -1 or url.find("#") != -1

def is_file(url):
    return url.find(".pdf") != -1 or url.find(".png") != -1 or url.find(".jpg") != -1 or url.find(".doc") != -1 or url.find(".ppt") != -1 or url.find(".rar") != -1 or url.find(".xls") != -1 or url.find(".mp4") != -1 or url.find(".mp3") != -1 or url.find(".wmv") != -1 or url.find(".zip") != -1  or url.find(".avi") != -1

def is_special_character(url):
    return (url.count(":") >= 2 and url.find("http") != -1) or url.find("|") != -1  or url.find("*") != -1

def is_too_deep(url):
    return url.count("/") >= 7

def link_parser(base_url ,raw_html):
    urls = []
    pattern_start = '<a href="'; pattern_end = '"'
    index = 0; length = len(raw_html)
    while index < length:
        start = raw_html.find(pattern_start, index)
        if start > 0:
            start = start + len(pattern_start)
            end = raw_html.find(pattern_end, start)
            link = raw_html[start:end]
            if len(link) > 0:
                link = urljoin(base_url, link)
                if link not in urls and is_ku(link) and not is_dynamic(link) and not is_file(link) and not is_special_character(link) and not is_too_deep(link):
                    urls.append(link)
            index = end
        else:
            break
    return urls

def read_robots(url, text):
    FIND = 0
    AGENT = 1
    disallows = []
    sitemaps = []
    lines = text.replace("\r", "").split("\n")
    state =  FIND
    for line in lines:
        if state == FIND:
            if line == "user-agent: *":
                state = AGENT
            elif line.find("sitemap") != -1:
                if len(line.split(" ")) >= 2:
                    sitemaps.append(line.split(" ")[1])
        elif state == AGENT:
                if line.find("disallow:") != -1:
                    if len(line.split(" ")) >= 2:
                        path = line.split(" ")[1]
                        disallows.append(urljoin(url, path))
                elif line.find("user-Agent") != -1:
                    state = FIND
                elif line.find("sitemap") != -1:
                    if len(line.split(" ")) >= 2:
                        sitemaps.append(line.split(" ")[1])
    return disallows, sitemaps

def create_directory_and_save(current_url, text):
    if current_url.find(".html") != -1 or current_url.find(".htm") != -1:
        if current_url[-1] == "/":
            current_url = current_url[:-1]
        url_split = current_url.split("//")[1]
        create_dir_name = current_url[:current_url.find(current_url.split("/")[-1])]
        create_dir_name = create_dir_name.replace("http://", "")
        create_dir_name = create_dir_name.replace("https://", "")
        create_dir_name = create_dir_name.replace(":", "-")

        print(create_dir_name)

        if not os.path.isdir(save_path + create_dir_name):
            os.makedirs(save_path + create_dir_name)

        f = open(save_path + url_split.replace(":", "-"), 'w', encoding="utf-8")
        f.write(text)
        f.close()

        global count
        count += 1

    path = urljoin(current_url, robot_path)
    print(path)
    robot_text, status = get_page(path)
    print(status) 
    if status == 200 and robot_text.find("</body>") == -1:
        url_split = path.split("//")[1]
        create_dir_name = path[:path.find(path.split("/")[-1])]
        create_dir_name = create_dir_name.replace("http://", "")
        create_dir_name = create_dir_name.replace("https://", "")
        create_dir_name = create_dir_name.replace(":", "-")

        print(create_dir_name)

        if not os.path.isdir(save_path + create_dir_name):
            os.makedirs(save_path + create_dir_name)

        f = open(save_path + create_dir_name + robot_path, 'w', encoding="utf-8")
        f.write(robot_text)
        f.close()

        disallows, sitemaps = read_robots(current_url, robot_text)
        global visited_q, frontier_q
        visited_q += disallows
        frontier_q += sitemaps

        robots_list.append(current_url)
        if sitemaps != []:
            sitemaps_list.append(current_url)


load = input("load queue?(y/n) : ")
if load == "y":
    with open("q.txt", "r", encoding="utf-8") as f:
        q = f.readlines()
        frontier_q = eval(q[1])
        visited_q = eval(q[2])
        robots_list = eval(q[3])
        sitemaps_list = eval(q[4])
        count = eval(q[5])

if not os.path.isdir(save_path):
   os.makedirs(save_path)

while count <= 11140:
    current_url = frontier_q[0]
    frontier_q = frontier_q[1:]
    visited_q.append(current_url)

    print(current_url)

    text, status = get_page(current_url)
    extracted_links = link_parser(current_url, text)

    if text != "" and status == 200:
        create_directory_and_save(current_url, text)
    
    for link in extracted_links:
        if link not in frontier_q and link not in visited_q:
            frontier_q.append(link)

    if text != "" and status == 200:
        with open('q.txt', 'w', encoding='utf-8') as f:
            f.write(str(current_url) + "\n")
            f.write(str(frontier_q) + "\n")
            f.write(str(visited_q) + "\n")
            f.write(str(robots_list) + "\n")
            f.write(str(sitemaps_list) + "\n")
            f.write(str(count) + "\n")

    print(count)

with open('list_robots.txt', 'w', encoding='utf-8') as f:
    for url in robots_list:
        f.write(url + "\n")

with open('list_sitemap.txt', 'w', encoding='utf-8') as f:
    for url in sitemaps_list:
        f.write(url + "\n")