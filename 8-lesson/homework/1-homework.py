#!/usr/bin/env python3
'''
Задание 1
Откройте файл mbox-short.txt, “прочитайте” каждую строку в этом файле и найдите
строки, соответствующие данной: “From Stephen.marquard@uct.ac.za Sat Jan 5
09:14:16 2008” . Затем распечатайте все ВХОДЯЩИЕ email адреса и их общее
количество. Для решения данной задачи используйте методы строк. (используйте
with open)
'''

with open('files/mbox-short.txt', 'r') as emailFile:
    cnt = 0
    for i in emailFile:
        if i.startswith('From: '):
            cnt += 1
            print(i.split()[1])
    print(f'Количество входящих писем: {cnt}')
