#!/usr/bin/env python3
'''
Задание 3
Создать класс Фигура с одним параметром (по схеме),

    от него унаследовать три подкласса с уникальными параметрами
    в каждом подклассе создать полезные методы
    Решить двумя способами, с помощью полиморфизма и без него
'''
class Figure:
    """common class for shapes and figures"""
    def __init__(self, name):
        self.name = name

class Triangle(Figure):
    """Three sides, 180 degrees"""
    def __init__(self, name, sideA, sideB, sideC):
        super(Triangle, self).__init__(name)
        self.sideA = sideA
        self.sideB = sideB
        self.sideC = sideC

    def Perimeter(self):
        """Find perimeter of given triangle"""
        return self.sideA + self.sideB + self.sideC

    def Area(self):
        """Find square of given triangle"""
        s = (self.sideA + self.sideB + self.sideC) / 2
        return round((s * (s - self.sideA) * (s - self.sideB) * (s - self.sideC)) ** 0.5, 4)


class Square(Figure):
    """Four sides, 180 degrees"""
    def __init__(self, name, sideA, sideB):
        super(Square, self).__init__(name)
        self.sideA = sideA
        self.sideB = sideB

    def Perimeter(self):
        """Find perimeter of given square"""
        return self.sideA * self.sideB * 2

    def Area(self):
        """Find square of given square"""
        return self.sideA * self.sideB


class Circle(Figure):
    """No sides, 360 degress"""
    def __init__(self, name, radius):
        super(Circle, self).__init__(name)
        self.radius = radius

    def Perimeter(self):
        """Find Perimeter of given circle"""
        return round(2 * 3.14 * self.radius, 4)

    def Area(self):
        """Find Area of given circle"""
        return round(3.14 * (self.radius ** 2), 4)


test1 = Triangle('Triangle', 3, 4, 5)
test2 = Square('Square', 4, 3)
test3 = Circle('Circle', 5)
print(test1.name)
print(test1.Perimeter())
print(test1.Area())

print(test2.name)
print(test2.Perimeter())
print(test2.Area())

print(test3.name)
print(test3.Perimeter())
print(test3.Area())
