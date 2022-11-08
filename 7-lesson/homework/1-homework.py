#!/usr/bin/env python3
'''
Задание 1
Напишите программу, которая запрашивает ввод двух значений. Если хотя бы одно
из них не является числом, то должна выполняться конкатенация, то есть
соединение, строк. В остальных случаях введенные числа суммируются.

Примеры выполнения программы:
    Первое значение: 4
    Второе значение: 5
    Результат: 9.0
    Первое значение: a
    Второе значение: 9
    Результат: a9
'''
import logging

logging.basicConfig(filename='1-homework.log', datefmt='%Y-%m-%d %H:%M:%S', format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')

while True:
    val1 = input("Введите первое значение: ")
    if not val1:
        break
    val2 = input("Введите второе значение: ")
    if not val2:
        continue

    try:
        val1, val2 = float(val1), float(val2)
    except Exception as error:
        logging.error(error)

    print(f"Результат: {val1 + val2}")
