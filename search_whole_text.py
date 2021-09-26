import requests
from bs4 import BeautifulSoup
import time


KEYWORDS = ['дизайн', 'фото', 'web', 'python']

response = requests.get('https://habr.com/ru/all/')
response.raise_for_status()

text = response.text
soup = BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article')
for article in articles:
    title = article.find('h2')
    link = title.find('a').attrs.get('href')
    url = 'https://habr.com' + link
    time.sleep(1)
    resp = requests.get(url)
    resp.raise_for_status()

    text = resp.text
    soup = BeautifulSoup(text, features='html.parser')
    artic = soup.find('article')
    article_text = artic.find('div', class_='tm-article-body')
    time.sleep(1)
    arts_text = [art_text.text for art_text in article_text]
    for art_text in arts_text:
        art_text_lower = art_text.lower()
        for keyword in KEYWORDS:
            if keyword in art_text_lower:
                title = artic.find('h1')
                dt = artic.find('time').attrs.get('title')
                print(f'<{dt}> - <{title.text}> - <{url}>')
