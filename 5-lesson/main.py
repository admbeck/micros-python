# list1 = [20, 50, '10', 1, 2, 100,10, 10, 4]
# cnt = list1.count('10')
# print(cnt)

# str1 = 'python'
# print(str1.count('y'))

# print(list1)
# list1.append(50)
# print(list1)
# list1.insert(30, 88)
# print(list1)
# list2 = []
# for i in range(10):
#     list2.append(i)
#
# print(list2)

# list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# list2 = ['a', 'b', 'c']
# for i in list2:
#     list1.append(i)
# list1.extend(list2)
# print(list1)
# list3 = list1 + list2
# print(list3)



# list1 = [222, 11, 22, 3333, 11]
# # print(list1)
# # # elem = list1.pop(1)
# # list1.remove(11)
# # print(list1)
# print(list1.index(11))
#list1 = [222, 11, 22, 3333, 11]

# list1.remove('banana')
# if not 'banana' in list1:
#     list1.append('banana')
#
# print(list1)



# list1 = [222, 11, 22, 3333, 11]
# list2 = list1
#
# print(list1)
# print(list2)
# print(id(list1))
# print(id(list2))
# list1.append("python")
# print(list1)
# print(list2)
# print(id(list1))
# print(id(list2))

# a = b = 12
# print(id(a))
# print(id(b))
# a += 1
# print(id(a))
# print(id(b))

# list1 = [1, 2, 3]
# list2 = list1.copy()
# print(id(list1))
# print(id(list2))
# print(list1)


# print(list2)
# list1.append(88)
# print(list1)
# print(list2)


# не путать list2 = list1 с list2 = list1.copy()

# name = 'p y t h o n'
# list1 = name.split()
# print(list1)
# str1 = '+'.join(list1)
# print(str1)


# list1 = []
# for i in range(10):
#     list1.append(i)
#
#
# list2 = [i for i in range(100)]


# list_nechet = [i for i in range(1, 100, 2)]
# list_chet = [i for i in range(0, 100, 2)]
# print(list_nechet)
# print(list_chet)


# list1 = []
# list2 = []
# for i in range(100):
#     if i % 2 == 0:
#         list1.append(i)
#     else:
#         list2.append(i)
# print(list1)
# print(list2)
#
# list1_v2 = [i for i in range(100) if i % 2 == 0]
# list2_v2 = [i for i in range(100) if i % 2 != 0]
# print(list1_v2)
# print(list2_v2)

# trash = [10, 'python', 50, 'linux', 55, 'windows']
# list1 = []
# list2 = []
# for i in trash:
#     if type(i) == int:
#         list1.append(i)
#     elif type(i) == str:
#         list2.append(i)
# print(list1)
# print(list2)
#
# list3 = [i for i in trash if type(i) == int]
# list4 = [i for i in trash if type(i) == str]
# print(list3)
# print(list4)

# numbers = [i for i in range(11)]
#
# for i in numbers:
#     print(i)
#     if i % 2 == 0:
#         print("Пропуск хода, возвращаюсь к циклу")
#         continue
#     print("Вывод числа на экран")


# products = ['bread', 'milk', 'banana']
# result = True
# while result:
#     user_text = input("Введите команду: ")
#     if (cnt := len(user_text.split())) == 2:
#         command, value = user_text.split()
#
#         if command == 'add':
#             if value in products:
#                 print(f"Продукт {value} уже есть в списке {products}")
#             else:
#                 products.append(value)
#                 print(f"Продукт {value} добавлен в список {products}")
#         elif command == 'delete':
#             if value in products:
#                 products.remove(value)
#                 print(f"Продукт {value} удалён из списка {products}")
#             else:
#                 print(f"Продукта {value} нет в списке {products}")
#     elif cnt == 1 and user_text == 'exit':
#         print("Выход")
#         #raise ("ValueError")
#         result = False
#
#     else:
#         print("Вы ввели не правильное значение, нужно два слова")

# import time
# start = round(time.time())
#
# lucky = 0
# for a in range(10):
#     for b in range(10):
#         for c in range(10):
#             for d in range(10):
#                 for e in range(10):
#                     for f in range(10):
#                         if a + b + c == d + e + f:
#                             print(f"Счастливый билет №{lucky}:  {a} {b} {c} {d} {e} {f}")
#                             lucky += 1
# print(f"Количество счастливых билетов: {lucky}")
# print(f"Всего {round(lucky * 100 / 999999, 2)} %")
#
# stop = round(time.time())
# print(f"Время потраченное на скрипт {stop - start} sec")

import time
start = round(time.time())


cnt = 0
for k1 in range(28):
    innerTikects = []
    rightBount1 = k1 if k1 <= 9 else 9
    for l1 in range(rightBount1+1):
        k2 = k1 - l1
        rightBount2 = k2 if k2 <= 9 else 9
        for l2 in range(rightBount2 + 1):
            k3 = k2 - l2
            if k3 <= 9:
                rightBound3 = k3 if k3 <= 9 else 9
                l3 = k3 if k3 <= rightBound3 else 0
                innerTikects.append( str(l1) + str(l2) + str(l3))
                print(innerTikects)

    # for value1 in innerTikects:
    #     for value2 in innerTikects:
    #         cnt += 1
    #         print(f"Счастливый билет № {cnt}  --- {value1}{value2}")


stop = round(time.time())
print(f"Время потраченное на скрипт {stop - start} sec")

