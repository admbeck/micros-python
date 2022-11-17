#!/usr/bin/env python3
'''
Задание 6
Есть два текстовых списка. Нужно вернуть один список объединенных слов.

Подаваемые данные: 2 списка
'''
list1, list2 = ['apple', 'banana', 'cherry'], ['orange', 'lemon', 'pineapple']
print(list(map(lambda x, y: x + y, list1, list2)))
