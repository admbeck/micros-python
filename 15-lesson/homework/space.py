#!/usr/bin/env python3
import requests
import unicodedata
import json
from bs4 import BeautifulSoup
from pprint import pprint

menu_text = {
        1: 'Новости',
        2: 'Астрономия',
        3: 'Полеты',
        4: 'Луна',
        5: 'Технологии',
        }

menu = {
        1: 'news',
        2: 'science-astronomy',
        3: 'spaceflight',
        4: 'topics/moon',
        5: 'tech-robots',
        }

print(f'Категории для парсинга')
for key, value in menu_text.items():
    print(f'{key}: {value}')

number = int(input('Введите номер категории: '))

if menu.get(number):
    CATEGORY = menu.get(number)
else:
    CATEGORY = 'news'

HOST = 'https://www.space.com/' + CATEGORY
HEADER = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

html = requests.get(HOST, headers=HEADER).text
soup = BeautifulSoup(html, 'html.parser')
declarations = soup.find_all('a', class_='article-link')

json_data = []
for declaration in declarations:
    img_link = declaration.find('img').get('data-pin-media')
    title = declaration.find('h3').get_text(strip=True)
    date = declaration.find('p', class_='byline').find('time').get_text()
    author = declaration.find('p', class_='byline').find('span').get_text(strip=True).lstrip('By')
    synopsis = declaration.find('p', class_='synopsis').get_text(strip=True)

    # full text
    # full_text_link = declaration.get('href')
    # full_text_html = requests.get(full_text_link, headers=HEADER).text
    # full_text_soup = BeautifulSoup(full_text_html, 'html.parser')
    # full_text_decs = full_text_soup.find_all('dev', 'bodyCopy')
    # full_text = []
    # for decs in full_text_decs:
    #     full_text.append(decs.get_text())
    print(full_text_soup)
    json_data.append({
        'title': unicodedata.normalize('NFKD', title),
        'date': unicodedata.normalize('NFKD', date),
        'author': unicodedata.normalize('NFKD', author),
        'synopsis': unicodedata.normalize('NFKD', synopsis),
        # 'full_text':unicodedata.normalize('NFKD', full_text),
        'img_link': unicodedata.normalize('NFKD', img_link)
        })

filename = CATEGORY.replace('/', '-')
with open(f'space_{filename}.json', mode='w', encoding='UTF-8') as file:
    json.dump(json_data, file, ensure_ascii=False, indent=4)
