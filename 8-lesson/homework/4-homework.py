#!/usr/bin/env python3
'''
Задание 4
Документ «article.txt» содержит следующий текст: (используйте open)
'''
artFile = open('files/article.txt', 'r')
words = []
for i in artFile:
    words.extend(i.rstrip('\n').split())

largest = []
for j in words:
    if len(max(words, key=len)) == len(j):
        largest.append(j)

print(f"Слова имеющие максимальную длину: {largest}")
artFile.close()
