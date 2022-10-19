# print('''
# text1
#      text2
#           text3
# ''')

# print('text1\n\t\ttext2\n\t\t\t\ttext3')

# totalMoney = 1000
# quantity = 3
# price = 450
# print(f'dfsfsdf {totalMoney} ijoioioio {quantity} jdfgdfgdf {price}')

# a = 'spam'
# b = 'eggs'
# print(a+b)

# text = 'hello'
# print(text)

#num1 = 5; num2 = 7

num1, num2 = 5, 7

# temp1 = num1
# temp2 = num2
# num1 = temp2
# num2 = temp1

#num1, num2 = temp2, temp1
#num1, num2 = num2, num1

# x, y, z = y, z, x

# print(num1, num2)
# a = b = 5
# print(a)
# print(b)
# a = 5
# a = a + 1
# # a += 1
#
# print(a == 4)

# string1 = "I love python"
# Срезы

# #print(string1)
# string2 = string1[2::]
# #print(string2)
# #  [start:stop:step]
# string3 = string1[-1::-1]
# print(string3)
# print(string1[-1])

#string1 = "I love python"
# lst1 = [111, 2222, 3333]
# cnt = len(lst1)
# print(cnt)

# Методы строк
#string1 = "I love python"
# string2 = string1.upper()
# string3 = string1.lower()    (Yes / No)  Yes, yes, YES
# print(string2)
# print(string3)
# print(string1)
# index = string1.find('love')
# print(index)
# print(string1[index::])
#print(string1.count('l'))
# string1 = "I love python"
# print(string1.startswith('I'))
# print(string1.endswith('python'))
# index = string1.find('go')
# print(index)

# string2 = string1.lower()
# string3 = string2.endswith('python')
#print(string3)
# string2 = string1.lower().endswith('python')
# print(string2)

# string1 = "I love Python"
# string2 = string1.replace('Python', 'linux')
# print(string2)
# print(string1)
# ip_addr = '''
# 192.168.8.1
# 192.168.8.116
# 192.168.8.125
# 192.168.8.133
# 192.168.8.137
# 192.168.8.138
# 192.168.8.178
# 192.168.8.185
# 192.168.8.199
# 192.168.8.204
# 192.168.8.255
# '''
# ip_addr2 = ip_addr.strip().split('\n')
# print(ip_addr2)
#
#
# for ip in ip_addr2:
#     print(f"ping {ip}")

# string10 = '      -192.168.19  -'
# print(string10)
# print(string10.strip().rstrip('-'))

# mac_windows = 'e4-95-6e-44-d8-e6'
# mac_linux = mac_windows.replace('-', ':')
#
# print(mac_windows)
# print(mac_linux)
# a = 12


# interface_conf = '''
# nmcli con mod {name} ipv4.ipaddr {ip_a}/{prefix}
# nmcli con mod {name} ipv4.gateway {gw}
# nmcli con mod {name} ipv4.dns {dns}
# nmcli con up {name}
# '''
#
# print(interface_conf.format(prefix='24', ip_a='192.168.8.5', name='eth0',  gw='192.168.8.1', dns='8.8.8.8'))


# num1 = 192
# num2 = bin(num1)
# print(num2[2::])


# header  = '{:<15} {:20} {:10} {}'
#
# line1 = header.format('interface', 'ip', 'prefix', 'gw')
# line2 = header.format(1, '192.168.8.2', '24', '192.168.8.1')
# line3 = header.format(2, '192.168.80.82', '30', '192.168.8.81')

# print(line1)
# print('-'*60)
# print(line2)
# print(line3)
# ip_addr ='{0} {1} {2} {3}\n{0:08b} {1:08b} {2:08b} {3:08b}'
# print(ip_addr.format(192, 168, 100, 25))

a = 12
print(f'dgdfgdfgdf {a}')







