#!/usr/bin/env python3
'''
Задание 1
Напишите функцию, чтобы найти максимальное из трех чисел
'''
def mymax(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


num1 = int(input())
num2 = int(input())
num3 = int(input())
print(mymax(num1, num2, num3))
