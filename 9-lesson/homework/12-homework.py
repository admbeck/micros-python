#!/usr/bin/env python3
'''
Задание 12
Создайте пакет ‘figures’, состоящий из трех подпакетов:
‘triangle’, ‘circle’, ‘square’.

В каждом подпакете будем иметь файл code.py, где создадим ряд функций:

– для пакета ‘circle’: функции circle_perimeter() – вычисляет длину окружности,
circle_area() – вычисляет площадь окружности. Еще заведем переменную
default_radius = 5, которая будет скрыта при импорте модуля. Ее назначение –
дефолтный радиус для окружности, если пользователь не введет свой. Обе функции
принимают на вход только радиус.

– для пакета ‘triangle’: функции triangle_perimeter() – вычисляет периметр
треугольника, triangle_area() – вычисляет площадь фигуры. Дополнительно
создадим три переменные (длины сторон треугольника): a = 7, b = 2, c = 8,
которые также не будут видны при импорте. На вход функциям передается длина
трех сторон (если пользователь ничего не введет, то используются значения по
умолчанию).

– для пакета ‘square’: функции square_perimeter() – вычисляет периметр
квадрата, square_area() – вычисляет площадь фигуры. Дополнительная переменная
a = 15 не доступна при импорте и принимается функциями, если пользователь не
предоставил свои размеры стороны квадрата.

Ваша итоговая задача – позволить человеку, загрузившему ваш пакет, иметь
возможность напрямую импортировать все функции из подпакетов. Например, он
может написать так: ‘from figure import circle_area’.
'''
from figures.circle.code import circle_area, circle_perimeter
from figures.triangle.code import triangle_area, triangle_perimeter
from figures.square.code import square_area, square_perimeter

print(circle_area(), circle_perimeter(), triangle_area(), triangle_perimeter(), square_area(), square_perimeter())
print(circle_area(20), circle_perimeter(4), triangle_area(4, 5, 3), triangle_perimeter(8, 10, 4), square_area(5), square_perimeter(9))
