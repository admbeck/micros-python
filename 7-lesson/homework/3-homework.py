#!/usr/bin/env python3
'''
Задание 3
Тот же самый пример, с сообщением после каждой итерации о том что элемент
N добавлен
'''
import logging

logging.basicConfig(filename='3-homework.log', datefmt='%Y-%m-%d %H:%M:%S', format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')

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
    finally:
        print(f"Элемент {i} добавлен")

print(num)
print(chr)
