#!/usr/bin/env python3
'''
Задание 9
Написать программу, которая спрашивает у пользователя три числа
и выводит количество совпадающих.
'''

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))

match = 0

if num1 == num2:
    match = 2
if num2 == num3:
    match = 2
if num3 == num1:
    match = 2

if num1 == num2 == num3:
    match = 3

print(f"Количество совпадающих чисел: {match}")
