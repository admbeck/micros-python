#!/usr/bin/env python3
'''
Задание 3
Напишите код программы, которая будет открывать файл «article.txt» и выводить
на печать построчно последние строки в количестве lines (число которую можно
запросить у пользователя). Число должно быть положительным (используйте with
open)
'''
while True:
    lines = int(input("Сколько последних строк распечатать: "))
    if lines > 0:
        break

with open('files/article.txt', 'r') as articleFile:
    fullText = []
    for i in articleFile:
        fullText.append(i.rstrip('\n'))

    fullText.reverse()

    for j in range(lines):
        print(fullText[j])
