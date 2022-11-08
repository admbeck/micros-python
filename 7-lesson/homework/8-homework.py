#!/usr/bin/env python3
'''
Задание 8
Следующий код работает отлично, если пользователь вводит цифровое значение,
но всегда есть НО:
'''
import logging

logging.basicConfig(filename='8-homework.log', datefmt='%Y-%m-%d %H:%M:%S', format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')

try:
    min = int(input("Введите первое число: "))
    max = int(input("Введите второе число: "))

    for i in range(min, max+1):
        print(f"Квадрат числа {i} равен {i*i}")
except ValueError as error:
    print("Вы ввели не число, попробуйте снова")
    logging.error(error)
