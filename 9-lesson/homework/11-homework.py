#!/usr/bin/env python3
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
