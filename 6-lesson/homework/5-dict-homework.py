#!/usr/bin/env python3
# Словари
'''
Задание 5
Составьте словарь расстояний между городами по формуле:
    sqrt((x1 - x2)^2 + (y1 - y2)^2)
'''
cities = {
'Moscow': (550, 370),
'London': (510, 510),
'Paris': (480, 480),
}

distances = {}

x1 = cities['Moscow'][0]
y1 = cities['Moscow'][1]
x2 = cities['London'][0]
y2 = cities['London'][1]
x3 = cities['Paris'][0]
y3 = cities['Paris'][1]

waterloo = round((((x2 - x3) ** 2 ) + ((y2 - y3) ** 2)) ** 0.5, 4)
borodino = round((((x3 - x1) ** 2 ) + ((y3 - y1) ** 2)) ** 0.5, 4)
crimea = round((((x1 - x2) ** 2 ) + ((y1 - y2) ** 2)) ** 0.5, 4)

distances.update({'London-Paris': f'{waterloo}'})
distances.update({'Moscow-London': f'{crimea}'})
distances.update({'Moscow-Paris': f'{borodino}'})

print(distances)
