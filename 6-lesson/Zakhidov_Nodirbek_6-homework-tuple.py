# Zakhidov Nodirbek
# Кортежи/множества
'''
Задание 1
Есть кортеж a = (1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89)

Выведите в отдельный кортеж числа, которые меньше или равны 5 и числа,
которые больше 5.
'''
a = (1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89)

d = list(a)
b = []
c = []
for i in d:
    if i <= 5:
        b.append(i)
    else:
        c.append(i)

b = tuple(b)
c = tuple(c)

print(f"Кортеж чисел меньше или равных 5 {b}")
print(f"Кортеж чисел больше 5 {c}")

'''
Задание 2
Вы принимаете от пользователя его имя, фамилию, возраст. Сохраните их в
соответствующие переменные. Сохраните полученные значения в список.
'''
user = []

name = input("Введите ваше имя: ")
user.append(name)

surname = input("Введите вашу фамилию: ")
user.append(surname)

age = input("Введите ваш возраст: ")
user.append(age)

user = tuple(user)

print(f"Кортеж данных пользователя: {user}")

'''
Задание 3
Напишите программу, которая принимает от пользователя секвенцию чисел,
разделенных запятой и пробелом. После чего запишите каждое число в кортеж.
'''
ask = input("Введите секвенцию чисел разделенных запятой и пробелом: ")

nums = tuple(ask.split(', '))
print(f"Кортеж чисел: {nums}")

'''
Задание 4
Напишите программу, которая будет принимать три имени в качестве входных данных
от пользователя в одном input() и превращать данные в кортеж, ну а затем
доставать их:
'''
ask = input("Введите три любых имени разделенные между собой пробелом: ")

names = tuple(ask.split())
print(f"Кортеж имен: {names}")
print(f"Первое имя: {names[0]}")
print(f"Второе имя: {names[1]}")
print(f"Третье имя: {names[2]}")

'''
Задание 5
Дан кортеж чисел numbers = (1, 2, 3, 4, 5, 6, 7). напишите программу, которая
превращает каждый элемент кортежа в его квадрат и образует второй кортеж.
'''
numbers = [1, 2, 3, 4, 5, 6, 7]
squares = numbers.copy()

for i in range(len(numbers)):
    squares[i] = squares[i] ** 2

numbers = tuple(numbers)
squares = tuple(squares)

print(f"Список чисел: {numbers}")
print(f"Список квадратов: {squares}")

'''
Задание 6
Напишите программу, которая выводит все четные числа из кортежа в исходном
порядке, и останавливается когда число равно 815.
'''
numbers = (386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958,743, 527)

evennums = []
for i in range(len(numbers)):
    if numbers[i] == 815:
        break
    elif numbers[i] % 2 == 0:
        evennums.append(numbers[i])
evennums = tuple(evennums)
print(evennums)

'''
Задание 7
Есть кортеж с данными numbers = (12, 33, 44, 33, 12, 45, 11, 55, ’44’, 30, 10),
создайте список и кортеж данных без дубликатов
'''
numbers = (12, 33, 44, 33, 12, 45, 11, 55, '44', 30, 10)
setnum = set(numbers)
tupnum = tuple(numbers)

print(setnum)

'''
Задание 8
Получите кортеж VLANов со строки:

общих vlan
vlan которые есть в config_sw1 но нет в config_sw2
уникальные vlan c двух сторон
все vlan без дубликатов
'''
config_sw1 = 'switchport trunk allowed vlan 10,20,30,40,50,70'
config_sw2 = 'switchport trunk allowed vlan 80,90,10,45,50,100'

vlans1 = set(config_sw1.split()[4].split(','))
vlans2 = set(config_sw2.split()[4].split(','))

common = vlans1.intersection(vlans2)
both = vlans1.difference(vlans2)
unique = vlans1.symmetric_difference(vlans2)
allvl = vlans1.union(vlans2)

print(common, both, unique, allvl, sep='\n')
