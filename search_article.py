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
    all_articles = article.find_all('div', class_='tm-article-snippet')
    time.sleep(3)
    all_articles_text = [all_article.text for all_article in all_articles]
    for articles_text in all_articles_text:
        articles_text_lower = articles_text.lower()
        for keyword in KEYWORDS:
            if keyword in articles_text_lower:
                title = article.find('h2')
                link = title.find('a').attrs.get('href')
                url = 'https://habr.com' + link
                dt = article.find('time').attrs.get('title')
                print(f'<{dt}> - <{title.text}> - <{url}>')
