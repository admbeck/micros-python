# list1 = ['a', 'b', 'c', 'd']
# for i in list1:
#     tuple1 = (list1.index(i), i)
#     print(tuple1)
# print()
# for i in enumerate(list1):
#     print(i)

# a = '55'
# print(type(a))
# a = int(a)
# print(type(a))
# a = str(a)
# print(type(a))

# a = int('101010101', 2)
# print(a)
# b = bin(a)
# print(str(b)[2:])
#
# c = hex(255)
# print(c)
#
#
# list1 = list("micros")
# print(type(list1))
# list1 = tuple(list1)
# print(type(list1))

# num1 = input("Введите число: ")
# num2 = input("Введите число: ")
#
# if num1.isdigit() and num2.isdigit():
#     num1, num2 = int(num1), int(num2)
#
#     if num1 < num2:
#         for item in range(num1, num2+1):
#             print(item)
#     elif num1 > num2:
#         num1, num2 = num2, num1
#         for item in range(num1, num2+1):
#             print(item)
#
# else:
#     print(f"Вы вели не числовое значение {num1} и {num2}")
# from os import listdir, path, stat
# from sys import argv
# import datetime
#
#
#
#
# if len(argv) > 1:
#     dirname = argv[1] + '\\'
# else:
#     dirname = '.\\'
#
#
# files = listdir(dirname)
#
# print(f"\nСодержимое папки: {dirname}\n")
# header_tables = "{:20} {:7} {}"
# print(header_tables.format('Создан', 'Тип', 'Имя'))
#
# for file in files:
#     fullName = dirname + file
#     created_time = str(datetime.datetime.fromtimestamp(int(stat(fullName).st_ctime)))
#
#     if path.isdir(fullName):
#         print(header_tables.format(created_time, 'Папка', file))
#     elif file.endswith('.lnk'):
#         print(header_tables.format(created_time, 'Ярлык', file))
#     elif path.isfile(fullName):
#         print(header_tables.format(created_time, 'Файл', file))
#
#
# print('-'*20)
# print(f"Кол-во объектов: {len(files)}")


# num1 = 1
# num2 = 'a'
#
# try:
#     num2 = int(num2)
#     print(num1/num2)
# except Exception as error:
#     print(error)
#     print(error.__class__)
#     print(error.__class__.__name__)


while True:

    try:

        num = input("Введите номер: ")
        if not num: break
        num = int(num)
        if num == 1:
            print(name)
        elif num == 2:
            list1 = [1, 2, 3]
            print(list1[10])
        elif num == 3:
            print(0 / 0)
        elif num == 4:
            int('a')
        elif num == 5:
            print("YES")
    # except Exception as e:
    # if e.__class__ is ValueError:
    #     print("Вы ввели не число")
    # elif e.__class__ is NameError:
    #     print("Данная переменная не существует")
    # elif e.__class__ is IndexError:
    #     print('Список оказался слишком мал')
    # elif e.__class__ is ZeroDivisionError:
    #     print("На ноль делить нельзя")

    except ValueError:
        print("Вы ввели не число")
    except NameError:
        print("Данная переменная не существует")
    except IndexError:
        print('Список оказался слишком мал')
    except ZeroDivisionError:
        print("На ноль делить нельзя")
    except:
        pass
    else:
        print("Ошибки не было, все нормально")
    finally:
        print("В любом случае распечатаю")
