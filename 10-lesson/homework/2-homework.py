#!/usr/bin/env python3
'''
Задание 2
С помощью функции filter выведите список оценок, которые больше 75.
'''
scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
print(list(filter(lambda x: x > 75, scores)))
