#!/usr/bin/env python3
'''
Задание 4
Составить программу, которая запрашивает ввод температуры тела человека и
определяет, здоров он или болен
'''
temp = float(input("Введите температуру: "))
# reference
# https://wikipedia.org/wiki/Human_body_temperature
print("Вы здоровы" if 37.5 > temp > 35.0 else "Срочно к врачу")
