#!/usr/bin/env python3
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
