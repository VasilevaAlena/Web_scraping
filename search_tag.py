import requests
from bs4 import BeautifulSoup
import time


KEYWORDS = {'Дизайн ', 'Python *', 'Учебный процесс в IT '}

response = requests.get('https://habr.com/ru/all/')
response.raise_for_status()

text = response.text
soup = BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article')
for article in articles:
    hubs = article.find_all('span', class_='tm-article-snippet__hubs-item')
    time.sleep(3)
    hubs_text = {hub.text for hub in hubs}
    if KEYWORDS & hubs_text:
        title = article.find('h2')
        link = title.find('a').attrs.get('href')
        url = 'https://habr.com' + link
        dt = article.find('time').attrs.get('title')
        print(f'<{dt}> - <{title.text}> - <{url}>')