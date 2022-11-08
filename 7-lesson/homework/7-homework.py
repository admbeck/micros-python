#!/usr/bin/env python3
'''
Задание 7
Замените первый if на try/except/else
'''
import sys
import logging

logging.basicConfig(filename='7-homework.log', datefmt='%Y-%m-%d %H:%M:%S', format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')

# if len(sys.argv) < 2:
#         print("Вы не указали название города")
#         print("Try again")
#         exit()
try:
    city = sys.argv[1]
    city = city.lower()


    if city == "tashkent"[0:len(city)]:
            print ("В Ташкенте тепло и солнечно")
    elif city == "london"[0:len(city)]:
            print ("В Лондоне пасмурно и сыро")
    elif city == "moskow"[0:len(city)]:
            print ("В Москве идёт сильный дождь")
    elif city == "paris"[0:len(city)]:
            print ("погода для романтики")
    elif city == "rio de janeyro"[0:len(city)]:
            print ("В Рио постоянно карнавалы")

    else:
            print ("прогноз не ясен, карантин")
except Exception as error:
    print("Вы не указали название города")
    print("Try again")
    logging.error(error)
