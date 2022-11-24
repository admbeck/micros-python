#!/usr/bin/env python3
"""
Задание 1
В примере найти и вывести трехзначные числа с помощью регулярных выражений.
"""
import re

sample = 'Exercises number 1, 12, 13, and 345 are important 456'

regex = r'\d{3}'
print(re.findall(regex, sample))
