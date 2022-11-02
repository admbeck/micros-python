#!/usr/bin/env python3
# Вложенность
'''
Задание 1
В задании создан словарь, с информацией о разных устройствах.

Необходимо запросить у пользователя ввод имени устройства (r1, r2 или sw1). И вывести информацию о соответствующем устройстве
'''
devices = {
    'r1': {
        'location': 'Bukhara',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.1'
    },
    'r2': {
        'location': 'Samarkand',
        'vendor': 'Cisco',
        'model': '4451',
        'ios': '15.4',
        'ip': '10.255.0.2'
    },
    'sw1': {
        'location': 'Tashkent',
        'vendor': 'Cisco',
        'model': '3850',
        'ios': '3.6.XE',
        'ip': '10.255.0.101',
        'vlans': '10,20,30',
        'routing': True
    }
}
devitem = list(devices.keys())
while True:
    while True:
        usrdev = input(f"Введите назание устройства [{'/'.join(devitem)}]: ")
        if not usrdev:
            print("До свидания")
            exit()
        elif usrdev not in devitem:
            continue
        else:
            break

    print(f"""
    Расположен\t{devices[usrdev]['location']}
    Вендор\t\t{devices[usrdev]['vendor']}
    Модель\t\t{devices[usrdev]['model']}
    Система (ios)\t{devices[usrdev]['ios']}
    IP адрес\t{devices[usrdev]['ip']}
    """)

    continue
