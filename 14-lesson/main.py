# class People:
#     legs = 2
#
#     def __init__(self, name, lastname, age):
#         self.name = name
#         self.lastname = lastname
#         self.age = age
#
#     def __str__(self):
#         return f'Класс People с полями: name={self.name} lastname={self.lastname} age={self.age}'
#
#     def say_about_you(self):
#         print(f'Меня зовут {self.name} {self.lastname} Мне {self.age} лет')
#
#
# class Employee(People):
#     def __init__(self, name, lastname, age, salary, workplace):
#         super(Employee, self).__init__(name, lastname, age)
#         # People.__init__(name, lastname, age)
#         self.salary = salary
#         self.workplace = workplace
#
#     def say_about_you(self):
#         print("Приоритет имеет локальный метод")
#
#
# worker = Employee('khasan', 'Khasan', 18, 10000, 'Micros')
# worker.say_about_you()
# print(worker.legs)


class Auto:
    def __init__(self, speed, model, kolesa=4):
        self.speed = speed
        self.model = model
        self.kolesa = kolesa

    def __str__(self):
        return f"Класс Auto с полми: скорость {self.speed} Модель {self.model} Колеса {self.kolesa} "


# class Tractor(Auto):
#     def __init__(self, speed, model, weight, work_time):
#         Auto.__init__(self, speed, model)
#         #super(Tractor, self).__init__(speed, model)
#         self.weight, self.work_time = weight, work_time
#
#     def say_about_you(self):
#         return f"Трактор с полями: Скорость {self.speed}, Модель {self.model}, Вес {self.weight}, Время работы {self.work_time}"
#
#     def __gt__(self, other):
#         return self.work_time > other.work_time
#
#     def __ge__(self, other):
#         return self.work_time >= other.work_time
#
#     def __lt__(self, other):
#         return self.work_time < other.work_time
#
#     def __le__(self, other):
#         return self.work_time <= other.work_time
#
#     def __ne__(self, other):
#         return self.work_time != other.work_time
#
#     def __eq__(self, other):
#         return self.work_time == other.work_time
#
#
# tr1 = Tractor(50, 'qwe', 100, 50)
# tr2 = Tractor(55, 'qwe', 900, 60)
#
# print(tr1 > tr2)
# print(tr1 >= tr2)
# print(tr1 <= tr2)
# print(tr1 < tr2)
# print(tr1 == tr2)
# print(tr1 != tr2)
# print(tr1.say_about_you())
# print(tr2.say_about_you())

#  ip route add 192.168.25.0/24 via 10.10.10.1
#  route add 192.168.25.0 mask 255.255.255.0 10.10.10.1 metric 10
#  ip route-static vpn-instance micros 192.168.25.0 255.255.255.0 10.10.10.1


# class Route:
#     def __init__(self, network, gw):
#         self.network = network
#         self.gw = gw
#
# class Linux(Route):
#     """ip route add 192.168.25.0/24 via 10.10.10.1"""
#     def __init__(self, network, gw, prefix):
#         super(Linux, self).__init__(network, gw)
#         self.prefix = prefix
#
#     def ip_route(self):
#         print(f"ip route add {self.network}/{self.prefix} via {self.gw}")
#
#
#
# class Windows(Route):
#     """route add 192.168.25.0 mask 255.255.255.0 10.10.10.1 metric 10"""
#     def __init__(self, network, gw, mask, metric):
#         super(Windows, self).__init__(network, gw)
#         self.mask = mask
#         self.metric = metric
#
#     def ip_route(self):
#         print(f'route add {self.network} mask {self.mask} {self.gw} metric {self.metric}')
#
#
# class HuaweiRouter(Route):
#     """ip route-static vpn-instance micros 192.168.25.0 255.255.255.0 10.10.10.1"""
#     def __init__(self, vrf, network, mask, gw  ):
#         super(HuaweiRouter, self).__init__(network, gw)
#         self.vrf = vrf
#         self.mask = mask
#
#     def ip_route(self):
#         print(f"ip route-static vpn-instance {self.vrf} {self.network} {self.mask} {self.gw}")
#
#
# device1 = Linux('192.168.25.0',  '10.10.10.1', '24')
# device2 = Windows('192.168.26.0', '255.255.255.0', '10.10.10.1', '10')
# device3 = HuaweiRouter('micros', '192.168.27.0', '255.255.255.0', '10.10.110.1')
#
# # device1.linux_ip_route()
# # device2.windows_ip_route()
# # device3.Huawei_ip_route()
#
# devices = [device1, device2, device3]
# # for dev in devices:
# #     if isinstance(dev, Linux):
# #         dev.linux_ip_route()
# #     elif isinstance(dev, Windows):
# #         dev.windows_ip_route()
# #     elif isinstance(dev, HuaweiRouter):
# #         dev.Huawei_ip_route()
#
# for dev in devices:
#     dev.ip_route()


# class Abc:
#     def public(self):
#         print("<имя_метода> без одного или двух нижних черточек в начале, это публичный")
#
#     def _protected(self):
#         print('''<имя_метода> c одним нижним подчеркиванием в начале, это защищённый метод,
#         можно обращаться внутри класса а так же под классом''')
#
#     def __private(self):
#         print("""<имя_метода> с двумя подчеркиванием, это приватный метод!
#         можно обращаться только внутри класса""")
#
# a = Abc()
# a.public()
# a._protected()
# #a.__private()
# a._Abc__private()


# class Ewo_odin_primer:
#     def __init__(self, x = 2):
#         self.__x = x
#
#     def kvadrat_chisla(self):
#         print(self.__x ** 2)
#
# matem = Ewo_odin_primer()
# matem.__x = 5
# matem._Ewo_odin_primer__x = 5
# matem.kvadrat_chisla()


from ping_micros import Network

ip100 = Network('192.168.8.0')
# ip100.hosts()
# ip100.subnet()
# ip100.binary()
# ip100.ping('10 20 30 40-50')
