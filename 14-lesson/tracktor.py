#!/usr/bin/env python3
class Auto:
    """docstring for Auto"""
    def __init__(self, speed, model, wheels = 4):
        self.speed = speed
        self.model = model
        self.wheels = wheels

    def __str__(self):
        """docstring for __str__"""
        return f"Класс Auto с полями: скорость {self.speed}, модель {self.model}, колеса {self.wheels}"

class Tractor:
    """docstring for Tractor"""
    def __init__(self, speed, model, weight, duration):
        super(Tracktor, self).__init__(speed, model)
        self.weight, duration = weight, duration

    def __str__(self):
        """docstring for __str__"""
        return f"Класс Tractor"
