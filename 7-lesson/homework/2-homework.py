#!/usr/bin/env python3
'''
Задание 2
Есть список: list1 = [1, ‘a’, 3, ‘b’, 5, ‘6’, 7, ‘8’, 9, ‘c’], необходимо
разделить на два списка, в первом только цифровые значения, а во втором только
строки
'''
import logging

logging.basicConfig(filename='2-homework.log', datefmt='%Y-%m-%d %H:%M:%S', format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')

list1 = [1, 'a', 3, 'b', 5, '6', 7, '8', 9, 'c']
num = []
chr = []
for i in list1:
    try:
        i / 2
        num.append(i)
    except Exception as error:
        logging.error(error)
        chr.append(i)

print(num)
print(chr)
