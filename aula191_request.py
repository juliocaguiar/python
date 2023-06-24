# pip install requests types-requests
# requests para requisições HTTP
import re

import requests
# pip install requests types-requests bs4
from bs4 import BeautifulSoup

# http:// -> 80
# https:// -> 433
url = 'http://localhost:3333/'

response = requests.get(url=url)
raw_html = response.content
parsed_html = BeautifulSoup(raw_html, 'html.parser', from_encoding='utf-8')

# if parsed_html.title is not None:
#     print(parsed_html.title.text)

top_jobs_heading = parsed_html.select_one('#intro > div > div > article > h2')

if top_jobs_heading is not None:
    article = top_jobs_heading.parent
    if article is not None:
        for p in article.select('p'):
            print(re.sub(r'\s{1,}', ' ', p.text).strip())

# print(response.text)
