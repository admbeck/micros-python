#!/usr/bin/env python3
'''
Задание 14
Получите список VLANов со строки:
config = 'switchport trunk allowed vlan 1,3,10,20,30,100'
['1', '3', '10', '20', '30', '100']
'''
config = 'switchport trunk allowed vlan 1,3,10,20,30,100'
vlans = config.split()[4].split(',')
print(vlans)
