#!/usr/bin/env python3
'''
Задание 6
Нарисуйте ёлку (вид ёлки произвольный), высоту ёлки должен задавать
пользователь
'''
while True:
    size = input("Высота елки: ")
    if size.isdigit():
        size = int(size)
        break
    else:
        continue

for i in range(size):
    # пустота
    print(" " * (size - i - 1), end="")

    # горизонталь
    rn = 2 * i + 1

    for j in range(rn):
        if i == 0:
            print("*", end="")
        elif j == 0:
            print("/", end="")
        elif j == rn - 1:
            print("\\", end="")
        else:
            print("#", end="")
    print()

if size > 5:
    print(" " * int(j/2 - 1), end="")
    print("| |")
else:
    print(" " * int(j/2), end="")
    print("|")
