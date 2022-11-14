#!/usr/bin/env python3
'''
Задание 10
Напишите функцию, которое принимает целое число и возвращает сумму цифр целого
числа 108 -> 9
'''
def numsum(onum):
    sum = 0
    for i in list(str(onum)):
        sum += int(i)
    return sum


num1 = int(input("Введите число: "))
print(f"{num1} -> {numsum(num1)}")
