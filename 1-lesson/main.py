# String1 = "Hello word"
# print(String1)

a = 2
b = 5
# tmp1 = a
# tmp2 = b
# a = tmp2
# b = tmp1
# a, b = tmp2, tmp1
# a, b = b, a
# print(a)
# print(b)
# a = 3
#a = a + 1
# a +=10

# print(a)

# print('Hello')
# print("Hello")
#print('11111\n222222\n333333\n\n\t\t444444')
# print('111','22222','22222', sep='-', end=' ')
# print('aaaaaa')


# print("Сегодня мы проёдем", end='\n *')
# print("тема1", end='\n *')
# print("ткма2", end='\n *')
# print("ткма2", end='\n *')
# print("ткма2")


# a = 2
# b = 4
# print("Сумма чисел", a, 'и', b, 'равен', a+b)
# print("Сумма чисел "+ str(a) + ' и ' + str(b) + ' равен', a+b)
#
# print(f"Сумма чисел {a} и {b} равен {a+b}")

# a = '2'
# b = '3.14'
# print(int(a) + float(b))
#
# a = int(input("Введите первое число: "))
# b = input("Введите второе число: ")
#
# # print(a+b)



# micros = "I love Python"
# print(micros)
# print(  micros.upper()  )
# print(  micros.lower()  )
# print(micros.startswith("I"))
# print(micros.endswith("on"))
# print(micros.split())

# ip = '''
# 192.168.157.255,
# 224.0.0.22,
# 224.0.0.251,
# 224.0.0.252,
# 224.0.0.253,
# 239.255.102.18,
# 239.255.255.250,
# '''

# ip_sep = ip.replace(',', '').split()
# print(ip_sep)
# print(ip_sep[2])
#
# num = '1, 2, 3, 4'
# print(num.replace(',', ' ').split())

# string1 = '+   oooo   -'
# print(string1.rstrip('-').lstrip('+').strip()  )

string1 = 'I love python'
print(string1.replace('python', 'linux'))
# string1[start:stop:step]
# string1[0:stop:1]
print(string1[::])
print(string1[2:6:])
print(string1[2:6:2])
# string1[start:stop:step]
print(string1[-1::-2])
print(string1[::2])

a = string1.count('p')
print(a)

print(string1.count('i'))

mac = "d8-bb-c1-1a-86-ee"
print(mac.replace("-", ':'))


