#!/usr/bin/env python3
'''
Задание 13
Обработать строку ospf_route и вывести информацию на стандартный поток вывода
как на картинке ниже:

Protocol:               OSPF
Network:                10.0.24.0/24
AD/Metric:              [110/41]
Next-Hop:               10.0.13.3
Last update:            3d18h
Outbound Interface:     FastEthernet0/0
'''
ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

rinfo = ospf_route.split()
rinfo = [i.replace(',', '') for i in rinfo]

if rinfo[0] == 'O':
    rinfo[0] = 'OSPF'
elif rinfo[0] == 'C':
    rinfo[0] = 'Directly Connected'
elif rinfo[0] == 'S':
    rinfo[0] = 'Static'
elif rinfo[0] == 'R':
    rinfo[0] = 'RIP'
elif rinfo[0] == 'B':
    rinfo[0] = 'BGP'
# И так далее

print(f"""Protocol:\t\t{rinfo[0]}
Network:\t\t{rinfo[1]}
AD/Metric:\t\t{rinfo[2]}
Next-Hop:\t\t{rinfo[4]}
Last update:\t\t{rinfo[5]}
Outbound Interface:\t{rinfo[6]}""")
