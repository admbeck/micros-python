#!/usr/bin/env python3
'''
Задание 6
Дописать код (нельзя использовать просто except)
'''
import logging

logging.basicconfig(filename='6-homework.log', datefmt='%y-%m-%d %h:%m:%s', format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')

my_dict ={"key1": "value1","key2": "value2","key3": "value3"}
search_key = "non-existent key"
try:
    print(my_dict[search_key])
except KeyError as error:
    print(f"Сорян, '{search_key}' это неправильный ключ!")
    logging.error(error)
