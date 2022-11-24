#!/usr/bin/env python3
"""
Задание 3
Найти в тексте время. Время имеет формат часы:минуты. И часы, и минуты состоят
из двух цифр, пример: 09:00. Напишите регулярное выражение для поиска времени в
строке: «Завтрак в 09:00». Учтите, что «37:98» – некорректное время.
"""
import re

text = ['Завтрак в 09:00', 'Завтрак в 90:00', 'Обед  в 13:00', 'Обед в 13:61',
        'Ужин в 19:05', 'Ужин в 37:98', 'Ужин в 24:01']
regex = r'\b(?:\d|[01]\d|2[0-3]):[0-5]\d|24:00'

for line in text:
    if re.search(regex,line):
        print(line)
