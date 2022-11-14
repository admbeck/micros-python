# print(10//3)
# print(10 % 3)
#
# print(divmod(10, 3))
#
# def dm(a, b):
#     return (a//b, a%b)
#
# print(dm(10, 3))
#
# from bib.microspoems import obrabotkastiha
#
# obrabotkastiha('pushkin.txt', 'poems.txt')
# obrabotkastiha('byron.txt', 'poems.txt')
# obrabotkastiha('romeo.txt', 'poems.txt')



# def max_number(num1):
#     global num2
#     num2 = 2
#     print(f"Глобальные переменные {a} и {num2}")
#     print(f"Локальные переменные {num1} и {num2}")
#     if num1 > num2:
#         return num1
#     elif num2 > num1:
#         return num2
#     else:
#         return
#
# a = 6
# num2 = 10
# print(num2)
# mn = max_number(a)
# print(mn)
# print(num2)

# def calc(a, b, action='+', verbose=False):
#     if action == '+':
#         if verbose:
#             return f"{a} {action} {b} = {a+b}"
#         else:
#             return a+b
#
#
# a = calc(2, 5)
# # b = calc(2, 5, '-')
# # c = calc(2, 5, '/')
# # d = calc(2, 5, '*')
# print(a)

# def basec_op(operator, value1, value2):
#     return eval(f"{value1}{operator}{value2}")
#
#
# res = basec_op('+', 4, 7)
# print(res)


# a = 6
# def answer(age=18):
#     age = check(age)
#     if age <= 18:
#         print('Вам нужно учиться')
#     elif 18 < age <= 50:
#         print('Вам нужно работать')
#     elif 50 < age <= 59:
#         print('Вам скоро на пенсию')
#     elif 60 < age <= 110:
#         print('Вы пенсионер')
#     else:
#         print('Сказочник')
#
#
# def check(age):
#     if age.isdigit():
#         return int(age)
#     else:
#         return 10
#
#
# answer('50')


# list1 = [1, 2, 3, 4, 5, 6]
#
# def from_int_to_str(list19):
#     return [str(i) for i in list19]
#
# list2 = from_int_to_str(list1)
# print(list2)

from algebra import num1num2

n
num1num2(1, 3)

def calculator(a, b, /,*, action="+",  verbose=False): #  параметр по умолчанию
    if action == '+':
        if verbose:
            return f"{a} + {b} = {a+b}"
        else:
            return a+b


range(10)
a = calculator( a=5, b=4, action="+", verbose=True)
print(a)