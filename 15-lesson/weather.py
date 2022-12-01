#!/usr/bin/env python3
import requests
from datetime import datetime
settings = {
        'appid': '136e508875e6cf6acd57ad8e3fa7a4fc',
        'units': 'metric',
        'lang': 'en'
    }

while True:
    city = input("Which country's location do you want to check? ")
    if not city: break
    settings['q'] = city

    data = requests.get('https://api.openweathermap.org/data/2.5/weather', params=settings).json()

    if data['cod'] != 200:
        print(data['message'])
        continue

    temp = data['main']['temp']
    cityName = data['name']
    timezone = data['timezone']
    wind = data['wind']['speed']
    sunrise = data['sys']['sunrise']
    sunset = data['sys']['sunset']
    description = data['weather'][0]['description']

    timestring = "%H:%M:%S"
    sunrise = datetime.utcfromtimestamp(int(sunrise + timezone)).strftime(timestring)
    sunset = datetime.utcfromtimestamp(int(sunset + timezone)).strftime(timestring)

    print(f"""In {cityName} it is {description} now.
Temperature is {temp}°C.
Wind speed is {wind} m/s.
Sun rises on {sunrise} and sets down on {sunset}""")
