#!/usr/bin/env python3
'''
Задание 9
Ловить ошибки это конечно здорово, но уметь логировать их и записывать в файл
еще лучше, задача разобраться со стандартной библиотекой logging
'''
import logging # Загрузка библиотеки

# logging.basicConfig(filename='my_error.log', datefmt='%Y-%m-%d %H:%M:%S', format='%(asctime)s\t%(levelname)s\t%(name)s\t%(message)s') # Файл появится в том каталоге где запущен скрипт
logger = logging

try:
    1/0
except ZeroDivisionError as error:
    logger.error(error)
