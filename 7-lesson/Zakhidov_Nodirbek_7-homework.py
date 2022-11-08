# Zakhidov Nodirbek
# break, continue, pass
'''
Задание 1
Есть список list1 = [i for i in range(100)], создайте новый список с пробросом
каждого пятого элемента (используйте continue)
'''
list1 = [i for i in range(100)]
list2 = []
for j in list1:
    if j % 5 != 0:
        continue
    else:
        list2.append(j)
print(list2)

'''
Задание 2
Напишите скрипт который будет работать циклично в интерактивном режиме, скрипт
должен запрашивать имя пользователя, если пользователь не вводя имя нажмет на
Enter то скрипт должен завершиться (используйте break)
'''
while True:
    name = input("Введите ваше имя: ")
    if not name:
        break
    print(name)

'''
Задание 3
Есть список: list1 = ['micros', 'python', 'linux', 'windows', 'bobo'], из него
составить новый список, но без буквы 'i', результат: list2 = ['mcros',
'python', 'lnux', 'wndows', 'bobo'] (используйте pass)
'''
list1 = ['micros', 'python', 'linux', 'windows', 'bobo']
list2 = []
for i in list1:
    tmp = []
    for j in i:
        if j == 'i':
            pass
        else:
            tmp.append(j)
    list2.append("".join(tmp))
print(list2)

# Try/except/finally/else
'''
Задание 1
Напишите программу, которая запрашивает ввод двух значений. Если хотя бы одно
из них не является числом, то должна выполняться конкатенация, то есть
соединение, строк. В остальных случаях введенные числа суммируются.

Примеры выполнения программы:
    Первое значение: 4
    Второе значение: 5
    Результат: 9.0
    Первое значение: a
    Второе значение: 9
    Результат: a9
'''
import logging

logging.basicConfig(filename='1-homework.log', datefmt='%Y-%m-%d %H:%M:%S', format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')

while True:
    val1 = input("Введите первое значение: ")
    if not val1:
        break
    val2 = input("Введите второе значение: ")
    if not val2:
        continue

    try:
        val1, val2 = float(val1), float(val2)
    except Exception as error:
        logging.error(error)

    print(f"Результат: {val1 + val2}")

'''
Задание 2
Есть список: list1 = [1, ‘a’, 3, ‘b’, 5, ‘6’, 7, ‘8’, 9, ‘c’], необходимо
разделить на два списка, в первом только цифровые значения, а во втором только
строки
'''
import logging

logging.basicConfig(filename='2-homework.log', datefmt='%Y-%m-%d %H:%M:%S', format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')

list1 = [1, 'a', 3, 'b', 5, '6', 7, '8', 9, 'c']
num = []
chr = []
for i in list1:
    try:
        i / 2
        num.append(i)
    except Exception as error:
        logging.error(error)
        chr.append(i)

print(num)
print(chr)

'''
Задание 3
Тот же самый пример, с сообщением после каждой итерации о том что элемент
N добавлен
'''
import logging

logging.basicConfig(filename='3-homework.log', datefmt='%Y-%m-%d %H:%M:%S', format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')

list1 = [1, 'a', 3, 'b', 5, '6', 7, '8', 9, 'c']
num = []
chr = []
for i in list1:
    try:
        i / 2
        num.append(i)
    except Exception as error:
        logging.error(error)
        chr.append(i)
    finally:
        print(f"Элемент {i} добавлен")

print(num)
print(chr)

'''
Задание 4
Приведенный ниже код назначает 5-ю букву каждого слова в food новый список
fifth. Однако код в настоящее время выдает ошибки. Вставьте предложение
try/except, которое позволит запустить код и создать список 5-й буквы в каждом
слове. Если слово недостаточно длинное, оно не должно ничего выводить.
Примечание. pass — Оператор является нулевой операцией; ничего не произойдет
при его выполнении.
'''
import logging

logging.basicConfig(filename='4-homework.log', datefmt='%Y-%m-%d %H:%M:%S', format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')

food = ["chocolate", "chicken", "corn", "sandwich", "soup", "potatoes", "beef", "lox", "lemonade"]
fifth = []
for x in food:
    try:
        fifth.append(x[4])
    except IndexError as error:
        logging.error(error)

print(fifth)

'''
Задание 5
Приведенный ниже код делит значения элемента на самого себя, но вылетает с
ошибками, необходимо учесть все типы ошибок и дописать код (условия цикла
менять нельзя, использовать полный синтаксис try/except/else)
'''
import logging

logging.basicConfig(filename='7-homework.log', datefmt='%Y-%m-%d %H:%M:%S', format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')

my_list = [2, "C", 10, "20", "micros", 50, 0, '0', '30']
for index in range(len(my_list)+5):
    try:
        print(f"{my_list[index]} / {my_list[index]} = {my_list[index] / my_list[index]}")
        print(f"Все получилось с первой попытки так как элемент '{my_list[index]}' является числом.")
    except Exception as e:
        if e.__class__.__name__ == 'IndexError':
            print(f"Список оказался слишком мал, индекс под номером {index} пуст")
        elif e.__class__.__name__ == 'ZeroDivisionError':
            print(f"На ноль делить нельзя")
        else:
            print(f"Ошибка {e.__class__.__name__} с элементом: '{my_list[index]}' так как тип элемента {type(my_list[index])}")
            try:
                tmp = int(my_list[index])
                if tmp == 0:
                    print(f"На ноль делить нельзя")
                else:
                    print(f"{tmp} / {tmp} = {tmp / tmp}")
                    print(f"Но я сконвертировал значение '{my_list[index]}' в число и результат уже распечатал")
            except:
                pass
            logging.error(e)

'''
Задание 6
Дописать код (нельзя использовать просто except)
'''
import logging

logging.basicconfig(filename='6-homework.log', datefmt='%y-%m-%d %h:%m:%s', format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')

my_dict ={"key1": "value1","key2": "value2","key3": "value3"}
search_key = "non-existent key"
try:
    print(my_dict[search_key])
except KeyError as error:
    print(f"Сорян, '{search_key}' это неправильный ключ!")
    logging.error(error)

'''
Задание 7
Замените первый if на try/except/else
'''
import sys
import logging

logging.basicConfig(filename='7-homework.log', datefmt='%Y-%m-%d %H:%M:%S', format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')

# if len(sys.argv) < 2:
#         print("Вы не указали название города")
#         print("Try again")
#         exit()
try:
    city = sys.argv[1]
    city = city.lower()


    if city == "tashkent"[0:len(city)]:
            print ("В Ташкенте тепло и солнечно")
    elif city == "london"[0:len(city)]:
            print ("В Лондоне пасмурно и сыро")
    elif city == "moskow"[0:len(city)]:
            print ("В Москве идёт сильный дождь")
    elif city == "paris"[0:len(city)]:
            print ("погода для романтики")
    elif city == "rio de janeyro"[0:len(city)]:
            print ("В Рио постоянно карнавалы")

    else:
            print ("прогноз не ясен, карантин")
except Exception as error:
    print("Вы не указали название города")
    print("Try again")
    logging.error(error)

'''
Задание 8
Следующий код работает отлично, если пользователь вводит цифровое значение,
но всегда есть НО:
'''
import logging

logging.basicConfig(filename='8-homework.log', datefmt='%Y-%m-%d %H:%M:%S', format='%(asctime)s:%(levelname)s:%(name)s:%(message)s')

try:
    min = int(input("Введите первое число: "))
    max = int(input("Введите второе число: "))

    for i in range(min, max+1):
        print(f"Квадрат числа {i} равен {i*i}")
except ValueError as error:
    print("Вы ввели не число, попробуйте снова")
    logging.error(error)

'''
Задание 9
Ловить ошибки это конечно здорово, но уметь логировать их и записывать в файл
еще лучше, задача разобраться со стандартной библиотекой logging
'''
import logging # Загрузка библиотеки

# logging.basicConfig(filename='my_error.log', datefmt='%Y-%m-%d %H:%M:%S', format='%(asctime)s\t%(levelname)s\t%(name)s\t%(message)s') # Файл появится в том каталоге где запущен скрипт
logger = logging

try:
    1/0
except ZeroDivisionError as error:
    logger.error(error)
