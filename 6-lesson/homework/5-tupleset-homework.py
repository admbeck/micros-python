#!/usr/bin/env python3
# Кортежи/множества
'''
Задание 5
Дан кортеж чисел numbers = (1, 2, 3, 4, 5, 6, 7). напишите программу, которая
превращает каждый элемент кортежа в его квадрат и образует второй кортеж.
'''
numbers = [1, 2, 3, 4, 5, 6, 7]
squares = numbers.copy()

for i in range(len(numbers)):
    squares[i] = squares[i] ** 2

numbers = tuple(numbers)
squares = tuple(squares)

print(f"Список чисел: {numbers}")
print(f"Список квадратов: {squares}")
