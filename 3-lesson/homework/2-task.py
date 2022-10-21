#!/usr/bin/env python3
'''
Задание 2
Дано 2 числа. Если их сумма кратна 5, прибавить 1, иначе вычесть 2
'''
#      float()?
num1 = int(input("Введите число 1: "))
num2 = int(input("Введите число 2: "))
sum = num1 + num2
print(sum + 1 if sum % 5 == 0 else sum - 2)
