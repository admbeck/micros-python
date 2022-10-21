#!/usr/bin/env python3
'''
Задание 6
Составить программу чтобы компьютер запросил имя пользователя и его год
рождения, затем подсчитал возраст человека, в зависимости от года рождения.
'''
from datetime import datetime

name = input("Введите имя: ")
year = int(input("Введите год рождения: "))

age = datetime.now().year - year
print(f"Привет {name}, тебе {age}.")
