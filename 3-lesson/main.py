# if/elif/else

# num1 = input("Введите первое число: ")
# num2 = input("Введите второе число: ")
#
# if num1.isdigit() and num2.isdigit():
#     num1, num2 = int(num1),  int(num2)
#     if num1 > num2:
#         print(f"Число {num1} больше чем число {num2}")
#     elif num1 < num2:
#         print(f"Число {num1} меньше чем число {num2}")
#     else:
#         print(f"Число {num1} равно {num2}")
# else:
#     print("Вы ввели не правильные числа")
#
# print("Конец кода")

# x = int(input())
# if x % 4 == 0:
#     print(f'Номер купе: {x // 4}')
# else:
#     print(f'Номер купе: {x // 4 + 1}')

# x = int(input())
# print(x//4 + (x % 4))

'''
1-10 Milk
11-20 Cheese
21-28 Meat
-     Holiday
'''
# day = 30
# if day >= 1 and day <= 10:
#     print('Milk')
# elif day >= 11 and day <= 20:
#     print('Cheese')
# elif day >= 21 and day <= 28:
#     print('Meat')
# else:
#     print('Holiday')


# from datetime import datetime
#
# current_time = datetime.now()
# current_time2 = datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
# current_time3 = datetime.now().strftime("%H:%M:%S")
#
# year = current_time.year
# day = current_time.day
# month = current_time.month
#
# time = current_time.time()
# hour = current_time.hour

# from datetime import datetime
# day = datetime.now().day
# if 1 <= day <= 10:
#     print('Milk')
# elif 11 <= day <= 20:
#     print('Cheese')
# elif 21 <= day <= 28:
#     print('Meat')
# else:
#     print('Holiday')

# Самая короткая форма if
# a = 4
# num = 0 if a % 4 == 0 else 1
# print(num)

# text = 'I love python'
# if (lenght := len(text)) > 5:
#     x = '1111'
#     print(lenght)
#
# print(lenght, '------')
# print(x)

import sys

if len(sys.argv) > 1:
    city = sys.argv[1]
else:
    city = input("Введите название города: ")
city = city.lower()

if city == 'tashkent'[:len(city)]:
    print(f'В Ташкент жарко')
elif city == 'moskow'[:len(city)]:
    print(f'В Москов идет дождь')
elif city == 'london'[:len(city)]:
    print(f'В Лондон идет снег')
elif city == 'rio de janeyro'[:len(city)]:
    print(f'В Рио идет карнавал')
else:
    print(f'Погода в городе {city} не известна')













