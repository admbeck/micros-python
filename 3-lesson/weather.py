#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    city = sys.argv[1]
else:
    city = input("Input city name: ")

city = city.lower()


if city == 'tashkent'[:len(city):]:
    print('It\'s hot in Tashkent.')
elif city == 'moscow'[:len(city):]:
    print('It\'s raining in Moscow')
elif city == 'london'[:len(city):]:
    print('It snows in London')
elif city == 'rio de janeiro'[:len(city):]:
    print('It\'s carnival time in Rio')
else:
    print(f'Weather in {city.capitalize()} is unknown')
