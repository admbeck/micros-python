#!/usr/bin/env python3
'''
Задание 2
Распечатать +, -, *, /, ^ следующих переменных:
    num1 = '3.14'
    num2 = '4'

3.14 + 4 = 7.14
3.14 - 4 = -0.86
3.14 * 4 = 12.56
3.14 / 4 = 0.785
3.14 ** 4 = 97.21
'''
num1 = '3.14'
num2 = '4'

num1 = float(num1)
num2 = int(num2)

sum = round(num1 + num2, 2)
sub = round(num1 - num2, 2)
mul = round(num1 * num2, 2)
div = round(num1 / num2, 3)
pwr = round(num1 ** num2, 2)

print(f'{num1} + {num2} = {sum}')
print(f'{num1} - {num2} = {sub}')
print(f'{num1} * {num2} = {mul}')
print(f'{num1} / {num2} = {div}')
print(f'{num1} ** {num2} = {pwr}')
