#!/usr/bin/env python3
# Словари
'''
Задание 3
Напишите код для суммирования всех значений словаря и вывод среднего
арифметического значения.
'''
num = int(input("Введите число: "))
dictionary = {}
for i in range(1, num + 1):
    dictionary.update({i: i ** 2})

print(f"Сумма всех значений: {sum(dictionary.values())}")
print(f"Среднее арифметическое: {sum(dictionary.values())/i}")
