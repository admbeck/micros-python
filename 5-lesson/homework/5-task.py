#!/usr/bin/env python3
'''
Задание 5
Напишите программу, которая будет принимать три имени в качестве входных данных
от пользователя в одном input() вызове функции.
'''
ask = input("Введите три любых имени разделенные между собой пробелом: ")

names = ask.split()
print(f"Первое имя: {names[0]}")
print(f"Второе имя: {names[1]}")
print(f"Третье имя: {names[2]}")
