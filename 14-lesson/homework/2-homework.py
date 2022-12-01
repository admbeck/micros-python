#!/usr/bin/env python3
'''
Задание 2
Создать Класс животное с одним параметром (по схеме)

    от него унаследовать четыре подкласса с уникальными параметрами
    затем создать по два объекта (экземпляра) от каждого подкласса
'''
class Animal:
    """Animal class"""
    def __init__(self, name):
        self.name = name

    def __str__(self):
        """docstring for __str__"""
        return f"Класс Animal с полем name {self.name}"


class Bird(Animal):
    """docstring for Bird"""
    def __init__(self, name, color, location, wingspan, diet):
        super(Bird, self).__init__(name)
        self.color = color
        self.location = location
        self.wingspan = wingspan
        self.diet = diet

    def __str__(self):
        """docstring for __str__"""
        return f"Класс Bird с полем name {self.name}, color {self.color}, location {self.location}, wingspan {self.wingspan}, diet {self.diet}"


class Mammal(Animal):
    """docstring for Mammal"""
    def __init__(self, name, color, location, size, diet):
        super(Mammal, self).__init__(name)
        self.color = color
        self.location = location
        self.size =  size
        self.diet = diet

    def __str__(self):
        """docstring for __str__"""
        return f"Класс Mammal с полем name {self.name}, color {self.color}, location {self.location}, size {self.size}, diet {self.diet}"


class Reptile(Animal):
    """docstring for Reptile"""
    def __init__(self, name, location, scalesize, size, diet):
        super(Reptile, self).__init__(name)
        self.location = location
        self.scalesize = scalesize
        self.size = size
        self.diet = diet

    def __str__(self):
        """docstring for __str__"""
        return f"Класс Reptile с полем name {self.name}, location {self.location}, scalesize {self.scalesize}, size {self.size}, diet {self.diet}"


class Fish(Animal):
    """docstring for Fish"""
    def __init__(self, name, location, color, diet):
        super(Fish, self).__init__(name)
        self.location = location
        self.color = color
        self.diet = diet

    def __str__(self):
        """docstring for __str__"""
        return f"Класс Fish с полем name {self.name}, location {self.location}, color {self.color}, diet {self.diet}"


eagle = Bird('Eagle', 'Brown', 'Sky', '1 m', 'Meat')
chicken = Bird('Chicken', 'White', 'Everywhere', '0.3 m', 'Seeds')
rat = Mammal('Rat', 'Black', 'Cities', '0.2 m', 'Everything')
monkey = Mammal('Monkey', 'Brown', 'Jungle', '1 m', 'Everything')
snake = Reptile('Snake', 'Desert', '0.3 cm', '1 m', 'Rodents')
chameleon = Reptile('Chameleon', 'Jungle', '0.02 cm', '0.2 m', 'Insects')
clownfish = Fish('Clownfish', 'Ocean', 'Orange', 'Plancton')
shark = Fish('Shark', 'Ocean', 'Grey', 'Other fish')

print(eagle)
print(chicken)
print(rat)
print(monkey)
print(snake)
print(chameleon)
print(clownfish)
print(shark)
