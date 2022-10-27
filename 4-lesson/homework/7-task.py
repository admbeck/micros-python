#!/usr/bin/env python3
'''
Задание 7
Написать программу «Банк». Вводится сумма вклада и количество лет. Рассчитать
сколько денег будет на счету пользователя к концу времени вклада. Решить
задачу по системе «сложный процент» (процент рассчитывается от новой суммы)
Годовой процент считать равным 10%.
'''

while True:
    money = input("Введите сумму вклада: ")
    years = input("Введите количество лет для вклада: ")
    if money.isdigit() and years.isdigit():
        money = float(money)
        years = int(years)
        break
    else:
        continue

percent = 1.1
for i in range(1, years + 1):
    money = money * percent
    print(f"{round(years, 2)} год: {round(money, 2)} $")

print(f"За {round(years, 2)} лет вы соберете: {round(money, 2)} $")
