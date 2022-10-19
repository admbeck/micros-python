#!/usr/bin/env python3
'''
Задание 3
Воспользуйтесь различными методами строк

python
PYTHON
python
'''

str1 = ' << pYthOn -   '
str2 = '   pYthOn \n .   '
str3 = ' (( pYthOn - :+   '

print(str1.strip(' <-').lower())
print(str2.strip(' .\n').upper())
print(str3.strip(' (-+:').lower())
