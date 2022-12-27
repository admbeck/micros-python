#!/usr/bin/env python3
import requests
from datetime import datetime

parameters = {
    'appid': '41e30429cbaedaabee3a2bd630d8fdb3',
    'units': 'metric',
    'lang': 'ru'
}

while True:
    city = input("Введите город, в котором хотите узнать погоду: ")
    if len(city) == 0: break
    parameters['q'] = city
    try:
        data = requests.get('https://api.openweathermap.org/data/2.5/weather', params=parameters).json()
        temp = data['main']['temp']
        city_name = data['name']
        wind = data['wind']['speed']
        timezone = data['timezone']
        sunrise = datetime.utcfromtimestamp(int(data['sys']['sunrise']) + int(timezone)).strftime('%Y-%m-%d %H:%M:%S')
        sunset = datetime.utcfromtimestamp(int(data['sys']['sunset']) + int(timezone)).strftime('%Y-%m-%d %H:%M:%S')
        description = data['weather'][0]['description']
        print(f'''
В городе \033[31m{city_name}\033[0m сейчас {description}
Температура: {temp} ℃
Скорость ветра: {wind} м/c
Рассвет: {sunrise}
Закат: {sunset} ''')
    except KeyError:
        print("Вы ввели не корректный город")
