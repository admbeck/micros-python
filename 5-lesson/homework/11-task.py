#!/usr/bin/env python3
'''
Задание 11
Подсчитайте общее количество цифр в числе.

Например, число 75869 , поэтому на выходе должно быть 5.
'''
numlist = []
number = input("Введите свое число: ")
for i in range(len(number)):
    numlist.append(number[i])

print(f"Кол-во цифр в числе {number} равно {len(numlist)}")
