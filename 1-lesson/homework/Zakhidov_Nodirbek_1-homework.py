# Захидов Нодирбек

# Урок №1, Задание №1
'''
спросить имя пользователя и поприветствовать его.
'''

name = input("Введите имя: ")
print("Привет, " + name)

# Урок №1, Задание №2
'''
сосчитать три числа и вывeсти их сумму.
'''

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))

print(f"Сумма чисел {num1}, {num2} и {num3} равно {num1 + num2 + num3}")

# Урок №1, Задание №3
'''
Задача:
    n школьников делят k яблок поровну, остаток остается в корзине.
    Сколько яблок достанется каждому школьнику?
    Сколько яблок останется в корзине?
'''

n = int(input("Введите количество школьников: "))
k = int(input("Введите количество яблок "))

pupils = int(k / n)
basket = int(k % n)

print("Кол-во яблок на каждого школьника:", pupils)
print("Кол-во яблок в корзине:", basket)

# Урок №1, Задание №4
'''
спросить число у пользователя и вернуть число до него и после
'''

number = int(input("Введите число: "))

print(f"Следующее число для {number} --> {number + 1}")
print(f"Предыдущее число для {number} --> {number - 1}")

# Урок №1, Задание №5
'''
вывести текст в правильно формате
Twinkle, twinkle, little star,
    How I wonder what you are!
        Up above the world so high,
        Like a diamond in the sky.
Twinkle, twinkle, little star,
        How I wonder what you are
'''

# Вариант 1
print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\t\tUp above the world so high,\n\t\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\t\tHow I wonder what you are")

# Вариант 2
print("Twinkle, twinkle, little star,")
print("\tHow I wonder what you are!")
print("\t\t\tUp above the world so high,")
print("\t\t\tLike a diamond in the sky.")
print("Twinkle, twinkle, little star,")
print("\t\tHow I wonder what you are")

# Вариант 3
print("""Twinkle, twinkle, little star,
    How I wonder what you are!
            Up above the world so high,
            Like a diamond in the sky.
Twinkle, twinkle, little star,
        How I wonder what you are""")

# Урок №1, Задание №6
'''
форматировать переменные в соответствии с результатом
У меня есть 1000 долларов, поэтому я могу купить 3 футбольных мяча за 450 долларов
'''

totalMoney = 1000
quantity = 3
price = 450

# Вариант 1
print("У меня есть " + str(totalMoney) + " долларов, поэтому я могу купить " + str(quantity) + " футбольных мяча за " + str(price) + " долларов")

# Вариант 2
print("У меня есть", totalMoney, "долларов, поэтому я могу купить", quantity, "футбольных мяча за", price, "долларов")

# Вариант 3
print(f"У меня есть {totalMoney} долларов, поэтому я могу купить {quantity} футбольных мяча за {price} долларов")

# Урок №1, Задание №7
'''
создать переменные "spam" и "eggs" и объединить их
'''

s = "spam"
e = "eggs"

# Без пробела
print(s + e)

# С пробелом
print(s, e)
