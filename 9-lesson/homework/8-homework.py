#!/usr/bin/env python3
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
