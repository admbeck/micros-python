#!/usr/bin/env python3
'''
Задание 8
Задача «Лесенка» По данному натуральному n ≤ 9 выведите лесенку из n ступенек,
i-я ступенька состоит из чисел от 1 до i без пробелов.
'''
while True:
    quant = input("Введите количество лесенок: ")
    if quant.isdigit():
        quant = int(quant)
        break
    else:
        continue

for i in range(1, quant + 1):
    for j in range(1, i + 1):
        print(j, end='')
    print()
