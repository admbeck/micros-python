# w = input()
# l = input()
# k = input()
#
#
# if w.isdigit() and k.isdigit() and l.isdigit():
#     k, w, l = int(k), int(w), int(l)
#     if k < w * l and (k % w == 0 or k % l == 0):
#         print('yes')
#     else:
#         print('no')
# else:
#     print("sdfsdf")


## циклы while/for
# x = 0
# while x < 11:
#     print(x)
#     x += 1
# else:
#     x = 0
# print(x)

# while True:
#     name = input("Введите своё имя: ")
#     if name:
#         print(f"Привет {name}")
#     else:
#         break
# else:
#     print("пока")

# bol = True
# while bol:
#     name = input("Введите своё имя: ")
#     if name:
#         print(f"Привет {name}")
#     else:
#         bol = False
# else:
#     print("пока")


# while True:
#     print("первый цикл")
#     while True:
#         print("второй цикл")
#         x = input()
#         if not x:
#             break


# while True:
#     city = input("Введите название города: ")
#     if not city:
#         break
#     city = city.lower()
#
#     if city == 'tashkent'[:len(city)]:
#         print(f'В Ташкент жарко')
#     elif city == 'moskow'[:len(city)]:
#         print(f'В Москов идет дождь')
#     elif city == 'london'[:len(city)]:
#         print(f'В Лондон идет снег')
#     elif city == 'rio de janeyro'[:len(city)]:
#         print(f'В Рио идет карнавал')
#     else:
#         print(f'Погода в городе {city} не известна')


# x = 0
# while x < 11:
#     if x == 5:
#         x += 1
#         continue
#     else:
#         print(x)
#         x += 1


# x = int(input("Введите число: "))
# while x > 0:
#     y = x
#     while y > 0:
#         y -= 1
#         print(f'Цикд внутри цикла x = {x} y = {y}')
#     print("Выход из внутренего цикла")
#     print("от х отнимаю 1")
#     x -= 1

# range(start,stop,step)
# range(0,10,1)

# for x in range(11):  # [2; 6)
#     print(x)

# for x in range(10, -1, -1):
#     print(x)


# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))
# if num1 > num2:
#     for i in range(num1, num2 - 1, -1):
#         print(f'Квадрат числа {i} равен {i*i}')
# else:
#     for i in range(num1, num2 + 1):
#         print(f'Квадрат числа {i} равен {i * i}')
# for b in range(1, 10):
#     for a in range(1, 10):
#         print(f"{a}*{b}={a*b}", end='\t')
#     print()


# rows = cnt = int(input("Введите число: "))

# for i in range(1, rows + 1):
#     for j in range(cnt):
#         print(i, end='')
#     cnt -= 1
#     print()

# from time import sleep
# for i in range(11):
#     print(f"\r{i}",  end='', flush=True )
#     sleep(1)

# for x in range(1 , 5):
#     print(x**2)
# else:
#     x = 0
#
# print(x)

####### LIST
# list1 = []
# list2 = ['яблоко', 'banana', 2, '10', 3.14, True]
# print(list1)
# print(list2)
#string = "10 20 30 40 50"
#list3 = string.split()

# string = "10,20,30,40,50"
# list3 = string.split(',')
# print(list3)

# name = 'python'
# list4 = list(name)
# print(list4)

# list1 = ['яблоко', 'банан', 'огурец', 20, 40, 'гастраном', 'asd', 'linux']
# print(list1[0])
# print(list1[1])
# print(list1[-1])

# list[start:stop:step]
# print(list1[1:5])
# print(list1[1:5:2])
# print(list1[::-1])
# print(list1[-2::-2])

# print(list1)
# list1[5] = "111111111"
# print(list1)

# list6 = [[1,
#           2,
#           3,
#           4,
#           5
#           ], ['один',
#               'два', 'три', 'четыре', 'пять']]
# print(list6)

# print(list6[0][2])

# list1 = [20, 50, 10, 1, 2, 100, 4]
# print(len(list1))
# var1 = sorted(list1)
# print(var1)
# print(list1)
#
# list1.sort()
# print(list1)


# list2 = ['Linux', 'apple', 'Apple', 'bob']
# list2.sort()
# print(list2)

# list1 = [20, 50, 10, 1, 2, 100, 4]
# print(sum(list1))
# print(min(list1))
# print(max(list1))
# list2 = [True, True, True, False, False]
# print(sum(list2))
# list1 = [20, 50, 10, 1, 2, 100, 4]
# list2 = []
# for i in list1:
#     list2.append(i*2)
# print(list1)
# print(list2)

# list1 = ['aaaa',  'bbbb', 'cccc']
#
# str1 = ''.join(list1)
# print(str1)

# name = "python"
# name1 = "python"
# name2 = "python"
# name4 = name+name1+name2
# print(name4)

# list1 = ['11', '222', '333']
# list2 = ['aaa', 'bbb', 'cccc']
# list3 = list1 + list2
# print(list3)
# list1.extend(list2)
# print(list1)

# TO BE CON







