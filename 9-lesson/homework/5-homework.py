#!/usr/bin/env python3
'''
Задание 5
Напишите функцию, для вычисления факториала числа (неотрицательное целое
число). Функция принимает число в качестве аргумента

5! = 1*2*3*4*5
'''
def factorial(onum):
    nums = [i for i in range(1, onum + 1)]
    print(f"{onum}! = {'*'.join(str(j) for j in nums)}")


num1 = int(input())
factorial(num1)
