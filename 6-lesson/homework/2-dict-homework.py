#!/usr/bin/env python3
# Словари
'''
Задание 2
Напишите сценарий Python для создания и печати словаря, содержащего число
(от 1 до n включительно) (где n — введенное пользователем число) в форме
(x, x * x).
'''
num = int(input("Введите число: "))
dictionary = {}
for i in range(1, num + 1):
    dictionary.update({i: i ** 2})

print(dictionary)
