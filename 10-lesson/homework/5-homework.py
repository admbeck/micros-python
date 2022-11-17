#!/usr/bin/env python3
'''
Задание 5
Есть список слов. Нужно с помощью map и lambda функции вернуть список длин
этих слов.
'''
words = ('apple', 'banana', 'cherry')
print(list(map(lambda x: len(x), words)))
