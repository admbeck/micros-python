#!/usr/bin/env python3
'''
Задание 1
Есть список list1 = [i for i in range(100)], создайте новый список с пробросом
каждого пятого элемента (используйте continue)
'''
list1 = [i for i in range(100)]
list2 = []
for j in list1:
    if j % 5 != 0:
        continue
    else:
        list2.append(j)
print(list2)
