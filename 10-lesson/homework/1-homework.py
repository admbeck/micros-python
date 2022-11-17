#!/usr/bin/env python3
'''
Задание 1
С помощью функции map выведите список имен с заглавной буквы.
'''
names = ['alfred', 'tabitha', 'william', 'arla']
print(list(map(lambda x: x.capitalize(), names)))
