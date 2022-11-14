#!/usr/bin/env python3
a, b, c = 7, 2, 8
def triangle_perimeter(a=a, b=b, c=c):
    return a + b + c


def triangle_area(a=a, b=b, c=c):
    s = (a + b + c) / 2
    return round((s * (s - a) * (s - b) * (s - c)) ** 0.5, 4)
