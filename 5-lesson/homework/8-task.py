#!/usr/bin/env python3
'''
Задание 8
Создайте переменную user_num, которая будет принимать от пользователя число.
Создайте числовой список от 1 до значения из переменной user_num (значение из
переменной включительно). Выведите сам список и сумму его чисел.
'''
user_num = int(input("Введите число: "))
sumlist = [i for i in range(1, user_num + 1)]
totalsum = 0
for j in range(len(sumlist)):
    totalsum += sumlist[j]

print(f"Список чисел в диапазоне от 1 до {j + 1}: {sumlist}")
print(f"Сумма списка чисел равна: {totalsum}")
