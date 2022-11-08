#!/usr/bin/env python3
'''
Задание 5
Приведенный ниже код делит значения элемента на самого себя, но вылетает с
ошибками, необходимо учесть все типы ошибок и дописать код (условия цикла
менять нельзя, использовать полный синтаксис try/except/else)
'''
import logging

logging.basicConfig(filename='7-homework.log', datefmt='%Y-%m-%d %H:%M:%S', format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')

my_list = [2, "C", 10, "20", "micros", 50, 0, '0', '30']
for index in range(len(my_list)+5):
    try:
        print(f"{my_list[index]} / {my_list[index]} = {my_list[index] / my_list[index]}")
        print(f"Все получилось с первой попытки так как элемент '{my_list[index]}' является числом.")
    except Exception as e:
        if e.__class__.__name__ == 'IndexError':
            print(f"Список оказался слишком мал, индекс под номером {index} пуст")
        elif e.__class__.__name__ == 'ZeroDivisionError':
            print(f"На ноль делить нельзя")
        else:
            print(f"Ошибка {e.__class__.__name__} с элементом: '{my_list[index]}' так как тип элемента {type(my_list[index])}")
            try:
                tmp = int(my_list[index])
                if tmp == 0:
                    print(f"На ноль делить нельзя")
                else:
                    print(f"{tmp} / {tmp} = {tmp / tmp}")
                    print(f"Но я сконвертировал значение '{my_list[index]}' в число и результат уже распечатал")
            except:
                pass
            logging.error(e)
