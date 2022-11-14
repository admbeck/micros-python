#!/usr/bin/env python3
'''
Задание 4
Напишите функцию, для переворота строки

Пример строки: 1234abcd
'''
def reverse(string):
    mstring = []
    for i in list(string)[::-1]:
        mstring.append(i)
    return "".join(mstring)


print(reverse('1234abcd'))
