#!/usr/bin/env python3
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
