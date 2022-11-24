#!/usr/bin/env python3
"""
Задание 5
Добавить регулярное выражения для поиска и вывода MAC адресов в скрипте который
работал с конфигурациями маршрутизатора (можно переделать весь скрипт для
работы с регуляркой)
"""
import re

macs = ['AA:AA:AA:FF:FF:FF',
        'AA-AA-AA-FF-FF-FF',
        'AAA.AAA.FFF.FFF',
        'AAA-AAA-FFF-FFF',
        'AAAA-AAFF-FFFF',
        'AAAA.AAFF.FFFF']

regex = r'(?:(?:[A-F]|[a-f])+[:.-]){2,5}(?:[A-F]|[a-f])+'
for mac in macs:
    if re.search(regex, mac):
        print(mac)
