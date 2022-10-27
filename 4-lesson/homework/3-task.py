#!/usr/bin/env python3
'''
Задание 3
Создайте игру «Угадай число», программа генирирует рандомное число в заданном
интервале, и предлагает пользователю угадать, игра продолжается до тех пор
пока пользователь угадает число, пример игры на картинке ниже:
    Python: Привет, как тебя зовут?
    Ваше имя: Хасан
    Python: Что ж, Хасан, я загадываю число от 1 до 5.
    Python: Попробуй угадать.
    Хасан: 5
    Python: Твое число слишком большое.
    Python: Попробуй угадать.
    Хасан: 1
    Python: Твое число слишком маленькое.
    Python: Попробуй угадать.
    Хасан: 3
    Python: Отлично, Хасан! Ты справился за 3 попытки.

можете сделать таймер
сделайте игру по уровням, первый уровень с 1 до 5,
второй уровень с 1 до 10 и.т.д.
'''
from random import randrange

while True:
    print("Python: Привет, как тебя зовут?")
    name = input("Ваше имя: ")
    if not name:
        break

    level = 1
    while True:
        maximum = 5 * level
        print("-"*20)
        print(f"Python: Уровень {level}")
        print(f"Python: Что ж, {name}, я загадываю целое число от 1 до {maximum}.")
        number = randrange(1, maximum + 1)
        att = 0

        while True:
            print("Попробуй угадать.")
            guess = input(f"{name}: ")
            att += 1

            if guess.isdigit() != True:
                print("Это не номер. Повторите снова.")
                continue

            guess = int(guess)
            if guess == number:
                print(f"Python: Отлично, {name}! Ты справился за {att} попытки.")
                cont = input("Python: Перейти на следующий уровень? [Y/n]")
                if not cont:
                    level += 1
                    break
                elif cont.lower()[:1] == 'y':
                    level += 1
                    break
                elif cont.lower()[:1] == 'n':
                    print(f"Python: Вы дошли до {level}-го уровня.")
                    exit()
            elif guess > number:
                print("Твое число слишком большое.")
            else:
                print("Твое число слишком маленькое.")
