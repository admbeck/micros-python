#!/usr/bin/env python3
'''
Задание 6
Напишите функцию, которая принимает строку и вычисляет количество букв верхнего
и нижнего регистра

Пример строки: 'The quick Brown Fox'
'''
def countchars(ostring):
    up = down = 0
    for i in ostring:
        if i.isupper():
            up += 1
        elif i.islower():
            down += 1

    print(f"Кол-во символов в верхнем регистре: {up}")
    print(f"Кол-во символов в нижнем регистре: {down}")

string = 'The quick Brown Fox'
countchars(string)
