#!/usr/bin/env python3
'''
Задание 9
Создайте два числовых списка от 1 до 100. Первый будет состоять только из
четных чисел, а второй из нечётных. Выведите сам список и сумму его чисел.
'''
allnums = [i for i in range(1, 100)]
oddnums = []
evennums = []
oddsum = 0
evensum = 0

for j in range(len(allnums)):
    if allnums[j] % 2 == 0:
        evennums.append(allnums[j])
        evensum += allnums[j]
    else:
        oddnums.append(allnums[j])
        oddsum += allnums[j]

print(f"Список четный чисел: {evennums}")
print(f"Сумма четных чисел: {evensum}")
print(f"Список нечетный чисел: {oddnums}")
print(f"Сумма нечетных чисел: {oddsum}")
