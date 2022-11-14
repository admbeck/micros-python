#!/usr/bin/env python3
'''
Задание 3
Напишите функцию, для умножения всех чисел в списке

Образец списка: (8, 2, 3, -1, 7)
'''
def mullist(olist):
    total = 1
    for i in olist:
        total *= i
    return total


tlist = (8, 2, 3, -1, 7)
print(mullist(tlist))
