# Zakhidov Nodirbek
'''
Задание 1
С помощью функции map выведите список имен с заглавной буквы.
'''
names = ['alfred', 'tabitha', 'william', 'arla']
print(list(map(lambda x: x.capitalize(), names)))

'''
Задание 2
С помощью функции filter выведите список оценок, которые больше 75.
'''
scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
print(list(filter(lambda x: x > 75, scores)))

'''
Задание 3
С помощью функции filter и Лямбда-функции выведите список слов-палиндромов.
'''
words = ['Anna', 'Alexey', 'Alla', 'Kazak', 'Dom']
print(list(filter(lambda x: x.lower() == x[::-1].lower(), words)))

'''
Задание 4
Напишите две функции (с генератором и без), которые будут формировать два
списка: list1 — это список четных чисел и list2 — это список не четных чисел.
Диапазон от 1 до n (n – это число, которое ввел юзер). Затем напишите к ней
декоратор, который будет выводить время потраченное на выполнение работы
функции, а также размер списка, который она сформировала.
'''
from datetime import datetime

def runSpeed(arg):
    def surround(*args, **kwargs):
        start = datetime.now()
        der = arg(*args, **kwargs)
        stop = datetime.now()
        print(f"Скорость выполнения: {stop - start}")
        return der
    return surround


@runSpeed
def generatorList(lng):
    list1 = [i for i in range(1, lng + 1) if not i % 2]
    list2 = [i for i in range(1, lng + 1) if i % 2]
    print("-"*5, "Герератор", "-"*5)
    print(f"Список четных чисел {list1}")
    print(f"Список нечетных чисел {list2}")


@runSpeed
def manualList(lng):
    list1 = []
    list2 = []
    for i in range(1, lng + 1):
        if i % 2:
            list2.append(i)
        else:
            list1.append(i)
    print("-"*5, "Вручную", "-"*5)
    print(f"Список четных чисел {list1}")
    print(f"Список нечетных чисел {list2}")


length = int(input("Введите длинну списка: "))
generatorList(length)
manualList(length)

'''
Задание 5
Есть список слов. Нужно с помощью map и lambda функции вернуть список длин
этих слов.
'''
words = ('apple', 'banana', 'cherry')
print(list(map(lambda x: len(x), words)))

'''
Задание 6
Есть два текстовых списка. Нужно вернуть один список объединенных слов.
Подаваемые данные: 2 списка
'''
list1, list2 = ['apple', 'banana', 'cherry'], ['orange', 'lemon', 'pineapple']
print(list(map(lambda x, y: x + y, list1, list2)))
