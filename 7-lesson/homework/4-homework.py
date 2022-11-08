#!/usr/bin/env python3
'''
Задание 4
Приведенный ниже код назначает 5-ю букву каждого слова в food новый список
fifth. Однако код в настоящее время выдает ошибки. Вставьте предложение
try/except, которое позволит запустить код и создать список 5-й буквы в каждом
слове. Если слово недостаточно длинное, оно не должно ничего выводить.
Примечание. pass — Оператор является нулевой операцией; ничего не произойдет
при его выполнении.
'''
import logging

logging.basicConfig(filename='4-homework.log', datefmt='%Y-%m-%d %H:%M:%S', format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')

food = ["chocolate", "chicken", "corn", "sandwich", "soup", "potatoes", "beef", "lox", "lemonade"]
fifth = []
for x in food:
    try:
        fifth.append(x[4])
    except IndexError as error:
        logging.error(error)

print(fifth)
