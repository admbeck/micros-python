#!/usr/bin/env python3
# Кортежи/множества
'''
Задание 8
Получите кортеж VLANов со строки:

общих vlan
vlan которые есть в config_sw1 но нет в config_sw2
уникальные vlan c двух сторон
все vlan без дубликатов
'''
config_sw1 = 'switchport trunk allowed vlan 10,20,30,40,50,70'
config_sw2 = 'switchport trunk allowed vlan 80,90,10,45,50,100'

vlans1 = set(config_sw1.split()[4].split(','))
vlans2 = set(config_sw2.split()[4].split(','))

common = vlans1.intersection(vlans2)
both = vlans1.difference(vlans2)
unique = vlans1.symmetric_difference(vlans2)
allvl = vlans1.union(vlans2)

print(common, both, unique, allvl, sep='\n')
