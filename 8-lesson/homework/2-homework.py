#!/usr/bin/env python3
'''
Задание 2
Откройте файл romeo.txt. “Прочитайте” в нем каждую строку. Получите отдельные
слова из каждой строки, после чего составьте список слов. В списке слова не
должны дублироваться. После чего распечатайте список, в котором все слова будут
отсортированы в алфавитном порядке. (используйте open)
'''
poemFile = open('files/romeo.txt', 'r', encoding='UTF-8')
fullText = []
for i in poemFile:
    fullText = fullText + i.split()
print(sorted(fullText))
poemFile.close()
