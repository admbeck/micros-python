#!/usr/bin/env python3
"""
Задание 2
Напишите регулярное выражение для поиска HTML-цвета, заданного как #ABCDEF,
то есть # и содержит затем 6 шестнадцатеричных символов.
"""
import re

colors = ['#ABCDEF', '#54#', '#F08080', '#FA8072', 'fghw3d', '#8B0000']

for color in colors:
    if re.search(r'#\w{6}\b', color):
        print(color)
