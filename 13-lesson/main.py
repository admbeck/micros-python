import csv

# name_1 = 'Anna'
# name_2 = 'Victor'
#
# with open('data.csv', mode='w') as file:
#     writer = csv.writer(file)
#     writer.writerow(
#         [name_1, name_2]
#     )

# with open('data.csv', mode='w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(
#         ("user_name", "address")
#     )
#
# user_data = [
#     ['user1', 'address1'],
#     ['user2', 'address2'],
#     ['user3', 'address3']
# ]
#
# for user in user_data:
#     with open("data.csv", mode='a', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(user)


# user_data = [
#     ("user_name", "address"),
#     ['user1', 'address1'],
#     ['user2', 'address2'],
#     ['user3', 'address3']
# ]
#
# with open('data2.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerows(user_data)

import csv, json
                                          # 'cp1251'
# with open("json_to_csv.csv", 'w', encoding="UTF-8", newline='' ) as file:
#     writer = csv.writer(file)
#     writer.writerow(
#         ("Имя", "Юзер", "Почта", "Телефон", "Адрес")
#     )

with open('users.json', encoding="UTF-8") as file:
    src = json.load(file)

# for a in src:
#     with open("json_to_csv.csv", 'a', encoding="UTF-8", newline='' ) as file:
#         writer = csv.writer(file)
#         writer.writerow(
#             (a['Имя'], a['Юзер'], a['Почта'], a['Телефон'], a['Адрес'])
#         )

with open('json_to_csv.csv', 'w', encoding="cp1251", newline='') as file:
    writer = csv.DictWriter(file, fieldnames="Имя Юзер Почта Телефон Адрес".split())
    writer.writeheader()
    for line in src:
        writer.writerow(line)

# json_data = []
# with open('json_to_csv.csv') as file:
#     reader = csv.reader(file)
#     headers = next(reader)
#
#     name, user, email, phone, address = headers
#     for line in reader:
#         json_data.append({
#             name: line[0],
#             user: line[1],
#             email: line[2],
#             phone: line[3],
#             address: line[4]
#         })
#
# print(json_data)

json_data = []
with open('json_to_csv.csv') as file:
    reader = csv.DictReader(file)

    for line in reader:
        json_data.append(line)

with open('csv_to_json_again.json', 'w', encoding='UTF-8') as file:
    json.dump(json_data, file, ensure_ascii=False, indent=4)
    






