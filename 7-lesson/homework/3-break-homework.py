#!/usr/bin/env python3
'''
Задание 3
Есть список: list1 = ['micros', 'python', 'linux', 'windows', 'bobo'], из него
составить новый список, но без буквы 'i', результат: list2 = ['mcros',
'python', 'lnux', 'wndows', 'bobo'] (используйте pass)
'''
list1 = ['micros', 'python', 'linux', 'windows', 'bobo']
list2 = []
for i in list1:
    tmp = []
    for j in i:
        if j == 'i':
            pass
        else:
            tmp.append(j)
    list2.append("".join(tmp))
print(list2)
