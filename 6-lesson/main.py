#### dict (словарь)
# # city = {}
# # city = dict()
#
# city = {'name': 'Tashkent', 'size': 30000, 'people': 35800, 'country': 'Uzbekistan'}
# city_v2 = dict(name='Tashkent', size=30000, people=35800, country='Uzbekistan')
#
# # print(city['name'])
# # print(city_v2['name'])
#
# city['size'] = 5500
# # print(city)
#
# city['location'] = {'ширата': 41, 'долгота': 69}
# city['temp'] = [14, 30, 16]
# # print(city)
# # print(city['location']['долгота'])
# # print(city['temp'][1])
# # print(city)
#
# # from pprint import pprint
# # pprint(city)
#
# print(city)
# print(sorted(city))
# print(len(city))
# print(sorted(city['temp']))
#
# temp = city.pop('name')
# print(city)
# print(temp)
# city['city_name'] = 'Tashkent'
# print(city)
# del city['city_name']
#
# # city = city.clear()
#
# #print(city['city_name'])
# print(city.get('temp', False))
# print('name_old3' in city)
# print('temp' in city)
#
# #if city.get('temp', False):
# # if 'name_old3' in city:
#
#
# city_v3 = city.copy()
# print(city_v3)
# print(type(city['temp'][0]))
# print(type(city))
#
# # print(city.keys())
# # print(city.values())
# # print(city.items())
#
# #key, value  = ('country', 'Uzbekistan')
# for key, value in city.items():
#     if value == 'Uzbekistan':
#         print(key)
#
# dic1 = {'name': 'linux', 'automation1': 'bash'}
# dic2 = {'tool': 'cli', 'automation': 'python'}
# dic1.update(dic2)
# print(dic1)


# action = ['like', 'dislike']
# all_action = dict.fromkeys(action, 0)
# print(all_action)
# all_action['like'] += 1
# all_action['like'] += 1
# all_action['like'] += 1
# all_action['like'] += 1
# all_action['dislike'] += 1
# all_action['dislike'] += 1
# all_action['dislike'] -= 1
# print(all_action)
#
#
# hello_dict = {i: 'Hello' for i in range(10)}
# print(hello_dict)

######## кортеж
# tuple1 = ('aaa', 'bbb', 'cccc', 1111, 1111, 1111)
# cnt = tuple1.count(1111)
# index = tuple1.index('cccc')
# print(cnt)
# print(index)
# print(tuple1[1])
# print(tuple1[1:])


# tuple1 = ('aaa', 'bbb', 'cccc', 1111, 1111, 1111)
# tuple1 = list(tuple1)
# tuple1.append(2222)
# tuple1 = tuple(tuple1)
#
# temp = ('python',)
# print(type(temp))

############  Множества (set)

# set1 = {10, 20, 10, 10, 50, 40}
# print(set1)
#
# list1 = set()
# print(type(list1))

# list1 = [10, 23, 10,  40]
# list1 = list(set(list1))
# list1.sort()
# print(list1)


# domain = ['olx.uz', 'distro.uz', 'olx.uz', 'ya.ru']
# domain = set(domain)
# domain.add('olx2.uz')
# domain.remove('olx.uz')
# print(domain)

# set1 = {1, 2, 3, 4}
# set2 = {2, 3, 6}
# set3 = set1.intersection(set2)
# print(set3)
# set4 = set1.difference(set2)
# print(set4)
# set5 = set1.symmetric_difference(set2)
# print(set5)
# set6 = set1.union(set2)
# print(set6)
#
# set7 = set("pythonn pythonn")
# print(set7)


############ Вложенность

users = [
    {
        'name': 'khasan',
        'lastname': 'karabaev',
        'friends': ['elyor', 'karim', 'timur'],
        'marks': {
            'math': 2,
            'history': 3,
            'izo': 4
        }
    },
    {
        'name': 'timur',
        'lastname': 'muhitddinov',
        'friends': ['elyor', 'karim', 'timur'],
        'marks': {
            'math': 5,
            'history': 4,
            'izo': 3
        }
    },
    {
        'name': 'otabek',
        'lastname': 'gulomjonov',
        'friends': ['abdu', 'jasur', 'timur'],
        'marks': {
            'math': 5,
            'history': 5,
            'izo': 3
        }
    }
]
# from pprint import pprint
# pprint(users)

# for user in users:
#     print(user['name'])
#     print(user['marks']['math'])


# average_history = 0
# for user in users:
#     print(user['name'])
#     print(user['marks']['math'])
#     average_history += user['marks']['history']
#
# average_history = average_history / len(users)
# print(average_history)


average_math = 0
average_history = 0
average_izo = 0
for user in users:
    print(user['name'])
    print(user['marks']['math'])
    average_history += user['marks']['history']
    average_math += user['marks']['math']
    average_izo += user['marks']['izo']


average_history = average_history / len(users)
average_math = average_math / len(users)
average_izo = average_izo / len(users)
print('-'*10)
print(average_history)
print(average_math)
print(average_izo)