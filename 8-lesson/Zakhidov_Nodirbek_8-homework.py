# Zakhidov Nodirbek
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

'''
Задание 5
print(test)
Объедините содержимое файлов pushkin.txt, byron.txt, romeo.txt в один файл
Poems.txt. (используйте with open и просто open)

** Разверните строки каждого стихотворения.

*** Постарайтесь придерживаться правильного выравнивание текста и чтоб знак
«=>» вставлялся ровно посередине каждого стихотворения (добейтесь результата в
точности как на картинке)
'''
with open('Poems.txt', 'w') as poems:
    with open('files/pushkin.txt', 'r') as pushkin:
        poem = []
        print('\t', '-'*8, 'pushkin.txt', '-'*8)
        for i in pushkin:
            poem.append(i.rstrip('\n'))
        for j in range(len(poem)):
            print('{:60} {}'.format(poem[j], poem[-j-1]))

    with open('files/byron.txt', 'r') as byron:
        poem = []
        print('\n\n\t', '-'*8, 'byron.txt', '-'*8)
        for i in byron:
            poem.append(i.rstrip('\n'))
        for j in range(len(poem)):
            print('{:60} {}'.format(poem[j], poem[-j-1]))

    with open('files/romeo.txt', 'r') as romeo:
        poem = []
        print('\n\n\t', '-'*8, 'romeo.txt', '-'*8)
        for i in romeo:
            poem.append(i.rstrip('\n'))
        for j in range(len(poem)):
            print('{:60} {}'.format(poem[j], poem[-j-1]))
