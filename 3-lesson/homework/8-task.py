#!/usr/bin/env python3
'''
Задание 8
 Напишите программу, которая принимает целое число от 1 до 12 и возвращает
 название месяца и количество дней.
'''
monthnum = int(input("Введите номер месяца: "))

if monthnum == 2:
    days = "28 или 29"
elif monthnum == 12:
    days = "31"
elif monthnum % 2 == 0:
    days = "30"
else:
    days = "31"

# Словарь нужен ой как
if monthnum == 1:
    month = "Январь"
elif monthnum == 2:
    month = "Февраль"
elif monthnum == 3:
    month = "Март"
elif monthnum == 4:
    month = "Апрель"
elif monthnum == 5:
    month = "Май"
elif monthnum == 6:
    month = "Июнь"
elif monthnum == 7:
    month = "Июль"
elif monthnum == 8:
    month = "Август"
elif monthnum == 9:
    month = "Сентябрь"
elif monthnum == 10:
    month = "Октябрь"
elif monthnum == 11:
    month = "Ноябрь"
elif monthnum == 12:
    month = "Декабрь"
else:
    print("Введен неверный месяц!")
    exit

print(f"Название месяца: {month}. Количество дней: {days}")
