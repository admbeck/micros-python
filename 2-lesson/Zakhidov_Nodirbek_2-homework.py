# Zakhidov Nodirbek
'''
Задание 1
Составить три формы присвоения переменной следующего вида x, y, z = y, z, x
'''
# 1)
x1, y1, z1 = 1, 2, 3

a1 = x1
x1 = y1
y1 = z1
z1 = a1

print(x1, y1, z1)

# 2)
x2, y2, z2 = 1, 2, 3

a2 = x2
b2 = y2
c2 = z2

x2 = b2
y2 = c2
z2 = a2

print(x2, y2, z2)

#3)
x3, y3, z3 = 1, 2, 3

x3, y3, z3 = y3, z3, x3

print(x3, y3, z3)

'''
Задание 2
Распечатать +, -, *, /, ^ следующих переменных:
    num1 = '3.14'
    num2 = '4'

3.14 + 4 = 7.14
3.14 - 4 = -0.86
3.14 * 4 = 12.56
3.14 / 4 = 0.785
3.14 ** 4 = 97.21
'''
num1 = '3.14'
num2 = '4'

num1 = float(num1)
num2 = int(num2)

sum = round(num1 + num2, 2)
sub = round(num1 - num2, 2)
mul = round(num1 * num2, 2)
div = round(num1 / num2, 3)
pwr = round(num1 ** num2, 2)

print(f'{num1} + {num2} = {sum}')
print(f'{num1} - {num2} = {sub}')
print(f'{num1} * {num2} = {mul}')
print(f'{num1} / {num2} = {div}')
print(f'{num1} ** {num2} = {pwr}')

'''
Задание 3
Воспользуйтесь различными методами строк

python
PYTHON
python
'''

str1 = ' << pYthOn -   '
str2 = '   pYthOn \n .   '
str3 = ' (( pYthOn - :+   '

print(str1.strip(' <-').lower())
print(str2.strip(' .\n').upper())
print(str3.strip(' (-+:').lower())

'''
Задание 4
Обработать переменные и получить результат:
    nohtyp evol I
    my friend
    плмрим
'''

string1 = 'I love python'
string2 = 'Hello my dear friend'
string3 = 'полиморфизм'

print(string1[::-1])
print(string2[6:9:] + string2[14::])
print(string3[::2])

'''
Задание 5
С помощью метода строк заменить слово show на display и создать другую переменную
'''
show = 'show ip interface brief'
display = show.replace('show', 'display')
print(display)

'''
Задание 6
В купейном вагоне имеется 9 купе с четырьмя местами для пассажиров в каждом. Напишите программу, которая определяет номер купе, в котором находится место с заданным номером (нумерация мест сквозная, начинается с 1).
'''
'''
     1     2      3       4       5       6      7       8        9
  +-------------------------------------------------------------------+
  | 1 2 | 5 6 | 9  10 | 13 14 | 17 18 | 21 22 | 25 26 | 29 31 | 33 34 |
  |     |     |       |       |       |       |       |       |       |
--| 3 4 | 7 8 | 11 12 | 15 16 | 19 20 | 23 24 | 27 28 | 30 32 | 35 36 |--
  +-------------------------------------------------------------------+
     O                                                            O
'''
num = int(input("Введите номер места (1-36): "))
print("Номер купе: ",int(num / 4) + (num % 4 > 0))
