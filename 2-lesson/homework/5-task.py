#!/usr/bin/env python3
'''
Задание 5
С помощью метода строк заменить слово show на display и создать другую переменную
'''
show = 'show ip interface brief'
display = show.replace('show', 'display')
print(display)
