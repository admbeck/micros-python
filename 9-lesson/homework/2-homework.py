#!/usr/bin/env python3
'''
Задание 2
Напишите функцию, для суммирования всех чисел в списке. Не использовать
встроенную функцию sum

Образец списка: (8, 2, 3, 0, 7)
'''
def sumlist(olist):
    total = 0
    for i in olist:
        total += i
    return total


tlist = (8, 2, 3, 0, 7)
print(sumlist(tlist))
