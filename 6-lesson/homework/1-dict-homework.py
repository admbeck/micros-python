#!/usr/bin/env python3
# Словари
'''
Задание 1
Есть два словаря, объедините их:
'''
dict1 = {
    'meat': 90,
    'milk': 15,
    'bread': 3,
    'potato': 6,
    'apple': 20,
    'banana': 25,
    'chicken wings': 45,
    'chocolate': 17
}
dict2 = {
    'kiwi': 30,
    'orange': 25,
    'coca-cola': 10,
    'chips': 18
}

dict1.update(dict2)
print(dict1)
