# Zakhidov Nodirbek
'''
Задание 1
Напишите функцию, чтобы найти максимальное из трех чисел
'''
def mymax(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


num1 = int(input())
num2 = int(input())
num3 = int(input())
print(mymax(num1, num2, num3))

'''
Задание 2
Напишите функцию, для суммирования всех чисел в списке. Не использовать
встроенную функцию sum

Образец списка: (8, 2, 3, 0, 7)
'''
def sumlist(olist):
    total = 0
    for i in olist:
        total += i
    return total


tlist = (8, 2, 3, 0, 7)
print(sumlist(tlist))

'''
Задание 3
Напишите функцию, для умножения всех чисел в списке

Образец списка: (8, 2, 3, -1, 7)
'''
def mullist(olist):
    total = 1
    for i in olist:
        total *= i
    return total


tlist = (8, 2, 3, -1, 7)
print(mullist(tlist))

'''
Задание 4
Напишите функцию, для переворота строки

Пример строки: 1234abcd
'''
def reverse(string):
    mstring = []
    for i in list(string)[::-1]:
        mstring.append(i)
    return "".join(mstring)


print(reverse('1234abcd'))

'''
Задание 5
Напишите функцию, для вычисления факториала числа (неотрицательное целое
число). Функция принимает число в качестве аргумента

5! = 1*2*3*4*5
'''
def factorial(onum):
    nums = [i for i in range(1, onum + 1)]
    print(f"{onum}! = {'*'.join(str(j) for j in nums)}")


num1 = int(input())
factorial(num1)

'''
Задание 6
Напишите функцию, которая принимает строку и вычисляет количество букв верхнего
и нижнего регистра

Пример строки: 'The quick Brown Fox'
'''
def countchars(ostring):
    up = down = 0
    for i in ostring:
        if i.isupper():
            up += 1
        elif i.islower():
            down += 1

    print(f"Кол-во символов в верхнем регистре: {up}")
    print(f"Кол-во символов в нижнем регистре: {down}")

string = 'The quick Brown Fox'
countchars(string)

'''
Задание 7
Напишите функцию, которая принимает слово и определяет является ли оно
палиндромом (палиндром — Слово или фраза, которые одинаково читаются слева
направо и справа налево.)
'''
def palindrome(ostring):
    strlist = list(ostring.lower())
    if strlist == strlist[::-1]:
        return 'является палиндромом'
    else:
        return 'не является палиндромом'


string = input()
print(f'Слово "{string}" {palindrome(string)}.')

'''
Задание 8
Пользователь делает вклад в размере n рублей сроком на years лет под 10%
годовых. Написать функцию bank, принимающая количество денег и лет, и
возвращающую сумму, которая будет на счете через years лет.
'''
def bank(cash, years):
    for i in range(1, years + 1):
        cash *= 1.1
    return cash


cash = float(input("Размер вклада: "))
years = int(input("Срок вклада: "))
print(f"Сумма по истечению срока: ${bank(cash, years)}")

'''
Задание 9
С помощью функции извлеките из списка числа, делимые на 15
'''
def divisive(onums):
    divlist = []
    for i in onums:
        if i % 15 == 0:
            divlist.append(i)
    return divlist


nums = [45, 55, 60, 37, 100, 105, 220]
print(divisive(nums))

'''
Задание 10
Напишите функцию, которое принимает целое число и возвращает сумму цифр целого
числа 108 -> 9
'''
def numsum(onum):
    sum = 0
    for i in list(str(onum)):
        sum += int(i)
    return sum


num1 = int(input("Введите число: "))
print(f"{num1} -> {numsum(num1)}")

'''
Задание 11
Напишите функцию, которая будет принимать количество секунд и возвращать их в
днях-часах-минутах-секундах

91000 секунд = 1 день, 1 час, 16 минут, 40 секунд
'''
def timeconvert(osec):
    sec = osec % 60
    min = osec // 60 % 60
    hour = osec // 60 // 60 % 60 % 24
    days = osec // 60 // 60 % 60 // 24
    return f"{days} день, {hour} час, {min} минут, {sec} секунд"


inputsec = 91000
print(f"{inputsec} секунд = {timeconvert(inputsec)}")

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
