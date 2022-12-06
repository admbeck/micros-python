# import requests
# from pprint import pprint
# from datetime import datetime
#
# parameters = {
#     'appid': '41e30429cbaedaabee3a2bd630d8fdb3',
#     'units': 'metric',
#     'lang': 'ru'
# }
#
# while True:
#     city = input('Введите название города для просмотра погоды: ')
#     if not city: break
#     parameters['q'] = city
#     data = requests.get('https://api.openweathermap.org/data/2.5/weather', params=parameters).json()
#     if data['cod'] != 200: break
#     temp = data['main']['temp']
#     city_name = data['name']
#     timezone = data['timezone']
#     wind = data['wind']['speed']
#     # datetime.utcfromtimestamp(числовой параметр).strftime(Формат времени)
#     #sunrise = data['sys']['sunrise']
#     sunrise = datetime.utcfromtimestamp(int(data['sys']['sunrise']) + int(timezone)).strftime("%Y-%m-%d %H:%M:%S")
#     # sunset = data['sys']['sunset']
#     sunset = datetime.utcfromtimestamp(int(data['sys']['sunset']) + int(timezone)).strftime("%Y-%m-%d %H:%M:%S")
#     description = data['weather'][0]['description']
#     print(f'''
# В городе \033[33m{city_name}\033[0m сейчас {description}
# Температура: {temp} °C
# Скорость ветра: {wind} м/c
# Рассвет: {sunrise}
# Закат: {sunset}
# ''')
#
#
#
#
from pprint import pprint

import requests
import unicodedata
from bs4 import BeautifulSoup
import json




menu_text = {
    1: 'Общество',
    2: 'Политика',
    3: 'Экономика',
    4: 'Спорт',
    5: 'Колумнисты',
    6: 'Коронавирус'
}

menu = {
    1: 'society',
    2: 'politics',
    3: 'economy',
    4: 'sport',
    5: 'column',
    6: 'coronavirus'
}
print(f"Категории для парсинга")
for key, value in menu_text.items():
    print(f'{key}: {value}')

number = int(input("Введите номер категории: "))

if menu.get(number):
    CATEGORY = menu.get(number)
else:
    CATEGORY = "society"

HOST = 'https://www.gazeta.uz/ru/' + CATEGORY
HEADER = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

html = requests.get(HOST, headers=HEADER).text
soup = BeautifulSoup(html, 'html.parser')
declarations = soup.find_all('div', class_='nblock')

json_data = []
for declaration in declarations:
    image_link = declaration.find('img').get('data-src')
    title = declaration.find('h3').get_text(strip=True)
    #publication = declaration.find('div', class_='ndt').get_text()
    #print(title)
    #print(publication)
    #print(image_link)

    if declaration.find('div', class_='ndt').find('span', class_='ico-comm'):
        # list1 = declaration.find('div', class_='ndt').get_text().split()
        # list1.pop()
        # publication = ' '.join(list1)
        end = len(declaration.find('div', class_='ndt').get_text().split()[-1])
        publication = declaration.find('div', class_='ndt').get_text()[:-end]
    else:
        publication = declaration.find('div', class_='ndt').get_text()

    description = declaration.find('p').get_text()

    json_data.append({
        'title': unicodedata.normalize('NFKD', title),
        'description': unicodedata.normalize('NFKD', description),
        'publication': unicodedata.normalize('NFKD', publication),
        'image_link': image_link
    })

with open(f'gazeta_{CATEGORY}.json', mode='w', encoding='UTF-8') as file:
    json.dump(json_data, file, ensure_ascii=False, indent=4)







