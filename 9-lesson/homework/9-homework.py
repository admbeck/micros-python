#!/usr/bin/env python3
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
