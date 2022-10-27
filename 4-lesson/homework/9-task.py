#!/usr/bin/env python3
'''
Задание 9
Последовательность Фибоначчи — это серия чисел. Следующее число находится
путем сложения двух чисел перед ним. В первые два числа 0 и 1 .
Например, 0 + 1 = 1
'''
while True:
    last = input("Конечный нормер Фибоначчи: ")
    if last.isdigit():
        last = int(last)
        break
    else:
        continue

a = 0
b = 1
print('0',end=' ')
while b < last + 1:
    a, b = b, a + b
    print(a,end=' ')
print()
