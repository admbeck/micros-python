# import sqlite3
#
# database = sqlite3.connect('../db/lesson17.db')
# cursor = database.cursor()
#
# cursor.execute('''
# SELECT * FROM students;
# ''')
# students = cursor.fetchall()
# print(students)
#
# name = 'Grisha'
# cursor.execute('''
# INSERT INTO  students(student_name) VALUES (?);
# ''', (name,))
# database.commit()
# database.close()


import requests
from datetime import datetime
import sqlite3

parameters = {
    'appid': '41e30429cbaedaabee3a2bd630d8fdb3',
    'units': 'metric',
    'lang': 'ru'
}

while True:
    city = input('Введите название города для просмотра погоды: ')
    if not city:
        database = sqlite3.connect('db_test.db')
        cursor = database.cursor()
        cursor.execute('''
        SELECT * FROM weather;
        ''')
        weather = cursor.fetchall()
        print(weather)
        database.close()
        break

    parameters['q'] = city
    data = requests.get('https://api.openweathermap.org/data/2.5/weather', params=parameters).json()
    if data['cod'] != 200: break
    temp = data['main']['temp']
    city_name = data['name']
    timezone = data['timezone']
    wind = data['wind']['speed']
    sunrise = datetime.utcfromtimestamp(int(data['sys']['sunrise']) + int(timezone)).strftime("%Y-%m-%d %H:%M:%S")
    sunset = datetime.utcfromtimestamp(int(data['sys']['sunset']) + int(timezone)).strftime("%Y-%m-%d %H:%M:%S")
    description = data['weather'][0]['description']
    print(f'''
В городе \033[33m{city_name}\033[0m сейчас {description}
Температура: {temp} °C
Скорость ветра: {wind} м/c
Рассвет: {sunrise}
Закат: {sunset}
''')

    database = sqlite3.connect('db_test.db')
    cursor = database.cursor()
    cursor.execute('''
    INSERT INTO weather(city,temp,wind,sunrise,sunset ) VALUES (?,?,?,?,?)
    ''', (city_name, temp, wind, sunrise, sunset ))

    database.commit()
    database.close()


