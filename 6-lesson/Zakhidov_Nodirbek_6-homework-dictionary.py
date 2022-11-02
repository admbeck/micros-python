# Zakhidov Nodirbek
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

'''
Задание 2
Напишите сценарий Python для создания и печати словаря, содержащего число
(от 1 до n включительно) (где n — введенное пользователем число) в форме
(x, x * x).
'''
num = int(input("Введите число: "))
dictionary = {}
for i in range(1, num + 1):
    dictionary.update({i: i ** 2})

print(dictionary)

'''
Задание 3
Напишите код для суммирования всех значений словаря и вывод среднего
арифметического значения.
'''
num = int(input("Введите число: "))
dictionary = {}
for i in range(1, num + 1):
    dictionary.update({i: i ** 2})

print(f"Сумма всех значений: {sum(dictionary.values())}")
print(f"Среднее арифметическое: {sum(dictionary.values())/i}")

'''
Задание 4
Напишите код для объединения двух списков в словарь ключ: значение.
СПИСКИ ДОЛЖНЫ БЫТЬ ОДНОГО РАЗМЕРА (содержимое списков произвольный)
'''
ips = ['192.168.20.1', '10.10.30.25', '172.16.3.40']
users = ['Вася Пупкин', 'Денис Уткин', 'Саша Дудкин']
userip = {}

for i in range(len(ips)):
    userip.update({users[i]: ips[i]})

print(userip)

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
