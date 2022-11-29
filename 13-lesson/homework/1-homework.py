#!/usr/bin/env python3
'''
Задание 1
Создать класс компьютер

    C параметрами: Владелец, Процессор, ОЗУ, Объём жесткого диска, Монитор
    Прописать метод строкового представления класса
    Создать метод который будет возвращать имя владельца компьютера:
        Запускать его самостоятельно (через указания вручную),
        Сделать чтоб он запускался в конструкторе (автоматически)
    Создать метод который будет сравнивать два класса по их ОЗУ
'''
class Computer:
    """Computer class"""
    def __init__(self, owner, cpu, ram, hdd, display):
        self.owner = owner
        self.cpu = cpu
        self.ram = ram
        self.hdd = hdd
        self.display = display
        self.ownerName()

    def __str__(self):
        """docstring for __str__"""
        return f"Class Computer with {self.owner} as owner, {self.cpu} as cpu, {self.ram} as ram, {self.hdd} as hdd and {self.display} as display"

    def ownerName(self):
        """Method to return owner's name (self.owner)"""
        print(f"My owner is {self.owner}.")

    def compareCpu(self, other):
        """docstring for compareCpu"""
        return self.cpu == other.cpu

pc1 = Computer('Vasya', 'Intel', '16 GB', '2 TB', 'FullHD')
pc2 = Computer('Borya', 'AMD', '32 GB', '1 TB', '4k')

print(pc1)
print(pc1.compareCpu(pc2))
