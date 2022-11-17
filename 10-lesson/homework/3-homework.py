#!/usr/bin/env python3
'''
Задание 3
С помощью функции filter и Лямбда-функции выведите список слов-палиндромов.
'''
words = ['Anna', 'Alexey', 'Alla', 'Kazak', 'Dom']
print(list(filter(lambda x: x.lower() == x[::-1].lower(), words)))
