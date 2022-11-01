#!/usr/bin/env python3
'''
Задание 6
Дан список чисел numbers = [1, 2, 3, 4, 5, 6, 7]. напишите программу, которая
превращает каждый элемент списка в его квадрат.
'''
numbers = [1, 2, 3, 4, 5, 6, 7]
squares = numbers.copy()

for i in range(len(numbers)):
    squares[i] = squares[i] ** 2

print(f"Список чисел: {numbers}")
print(f"Список квадратов: {squares}")
