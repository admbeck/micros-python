#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
CATEGORY = 'society'
HOST = 'https://www.gazeta.uz/ru/' + CATEGORY
HEADER = {
    'agent' = 'Mozilla/5.0 (X11; Linux x86_64; rv:107.0) Gecko/20100101 Firefox/107.0'
    }
html = requests.get(HOST, headers=HEADER)
soup = BeautifulSoup(html, 'html.parser')
declarations = soup.find_all('div', class_='nblock')
for declaration in declarations:
    image_link = declaration.find('img').get('data-src')
    title = declaration.find('h3').get_text(strip=True)
    date = declaration.find('div', class_='ndt').get_text(strip=True)

print(soup)
