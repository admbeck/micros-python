from functools import total_ordering


@total_ordering
class People:
    legs = 2

    def __init__(self, name, lastname, age):
        """То что запускается (типа) первым, инициализация класса"""
        self.name = name
        self.lastname = lastname
        self.age = age
        self.say_about_you()

    def __str__(self):
        """Строковое представления класса"""
        return f"Класс People c полями: name = {self.name} lastname={self.lastname} age={self.age}"

    def say_about_you(self):
        """Метод"""
        print(f"Меня зовут {self.name} {self.lastname} Мне {self.age} Лет")

    def god_rojdeniya(self):
        return 2022 - self.age

    def __eq__(self, other):
        return self.age == other.age

    def __lt__(self, other):
        return self.age < other.age


user1 = People('Vasya', 'Pupkin', 18)
user2 = People('Rafa', 'Ddos', 20)

print(user1 == user2)
print(user1 > user2)
print(user1 >= user2)
print(user1 < user2)
print(user1 <= user2)

# print(user1.god_rojdeniya())
# print(user2.god_rojdeniya())

# print(user1.name)
# print(user2.name)
#
# print(user1)
# print(user2)

# print(user1.say_about_you())
# print(user2.say_about_you())
