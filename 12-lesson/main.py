#!/usr/bin/env python3
import requests
import json
from pprint import pprint

api = 'https://jsonplaceholder.typicode.com/users'
users = requests.get(api).json()

json_file= []
for user in users:
    name = user['name']
    username = user['username']
    email = user['email']
    phone = user['phone']
    address = f"Город: {user['address']['city']}, улица: {user['address']['street']}, дом: {user['address']['suite']}"

    json_file.append({
        'Юзер': username,
        'Имя': name,
        'Почта': email,
        'Телефон': phone,
        'Адрес': address
    })

with open('users.json', 'w', encoding='UTF-8') as file:
    json.dump(json_file, file, ensure_ascii=False, indent=4)
