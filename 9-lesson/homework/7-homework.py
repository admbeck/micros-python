#!/usr/bin/env python3
'''
Задание 7
Напишите функцию, которая принимает слово и определяет является ли оно
палиндромом (палиндром — Слово или фраза, которые одинаково читаются слева
направо и справа налево.)
'''
def palindrome(ostring):
    strlist = list(ostring.lower())
    if strlist == strlist[::-1]:
        return 'является палиндромом'
    else:
        return 'не является палиндромом'


string = input()
print(f'Слово "{string}" {palindrome(string)}.')
