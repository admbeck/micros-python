#!/usr/bin/env python3
'''
Задание 4
Напишите две функции (с генератором и без), которые будут формировать два
списка: list1 — это список четных чисел и list2 — это список не четных чисел.
Диапазон от 1 до n (n – это число, которое ввел юзер). Затем напишите к ней
декоратор, который будет выводить время потраченное на выполнение работы
функции, а также размер списка, который она сформировала.
'''
from datetime import datetime

def runSpeed(arg):
    def surround(*args, **kwargs):
        start = datetime.now()
        der = arg(*args, **kwargs)
        stop = datetime.now()
        print(f"Скорость выполнения: {stop - start}")
        return der
    return surround


@runSpeed
def generatorList(lng):
    list1 = [i for i in range(1, lng + 1) if not i % 2]
    list2 = [i for i in range(1, lng + 1) if i % 2]
    print("-"*5, "Герератор", "-"*5)
    print(f"Список четных чисел {list1}")
    print(f"Список нечетных чисел {list2}")


@runSpeed
def manualList(lng):
    list1 = []
    list2 = []
    for i in range(1, lng + 1):
        if i % 2:
            list2.append(i)
        else:
            list1.append(i)
    print("-"*5, "Вручную", "-"*5)
    print(f"Список четных чисел {list1}")
    print(f"Список нечетных чисел {list2}")


length = int(input("Введите длинну списка: "))
generatorList(length)
manualList(length)
