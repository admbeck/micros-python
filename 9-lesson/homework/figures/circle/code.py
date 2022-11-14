#!/usr/bin/env python3
default_radius = 5
def circle_perimeter(circle_radius=default_radius):
    return round(2 * 3.14 * circle_radius, 4)


def circle_area(circle_radius=default_radius):
    return round(3.14 * (circle_radius ** 2), 4)
