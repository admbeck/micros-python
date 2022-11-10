# file = open('byron.txt', encoding='UTF-8')
# content = file.read().split()
#
# print(content)
# print(f"количество слов в файле: {len(content)}")
# file.close()


# file = open('byron.txt', encoding='UTF-8')
# for line in file:
#     print(line.rstrip())
#
# file.close()


# test = open('test.txt', mode='w', encoding='UTF-8')
# test.write('22222')
# test.close()


# test = open('test.txt', mode='w', encoding='UTF-8')
# test.write('111111\n')
# test.close()
# test = open('test.txt', mode='a', encoding='UTF-8')
# test.write('111111\n')
# test.close()

# test = open('test.txt', mode='w', encoding='UTF-8')
# for i in range(100):
#     test.write(f"Проход номер {i}, Привет\n")
#
# for i in range(100):
#     test.write(f"Проход номер {i}, ПОКА\n")
# test.close()


# file1 = open('pushkin.txt', encoding='UTF-8')
# content = file1.read()
#
# file2 = open('pushkin2.txt', 'w', encoding='UTF-8')
# file2.write(content)
#
# file1.close()
# file2.close()

# try:
#     with open('pushkin.txt', encoding='UTF-8') as file1:
#         content = file1.read()
#         print(file1.closed)
#         raise OSError("Синтактическая соль")
# except:
#     pass
#
# print(file1.closed)

# with open('pushkin3.txt', 'w', encoding='UTF-8') as file1:
#     with open('files/pushkin.txt', encoding='UTF-8') as file2:
#         content = file2.read()
#         file1.write(content)


# with open('pushkin4.txt', 'w', encoding='UTF-8') as file1, open('files/pushkin.txt', encoding='UTF-8') as file2:
#     content = file2.read()
#     file1.write(content)

# with open('nature.jpg', mode='rb') as file1:
#     content = file1.read()
#     for i in range(10):
#         file = open(f'nature_{i}.jpg', mode='wb')
#         file.write(content)
#         file.close()


# cnt = {}
# with open('mbox-short.txt', encoding='UTF-8') as file:
#     for line in file:
#         if line.startswith('From '):
#             # data = line.split()
#             # time = data[-2]
#             # hour = time.split(':')[0]
#
#             hour = line.split()[-2].split(':')[0]
#             cnt[hour] = cnt.get(hour, 0) + 1
#
#             # print(hour)
#             # print(cnt)
#
# for key in sorted(cnt):
#     print(f"В {key} часов пришло {cnt[key]} писем")




interfaces = []
with open('show_ip_int_brief.txt') as file:
    for line in file:
        if line.split()[-2] == 'up':
            int_name = line.split()[0].split('(')[0]
            interfaces.append(int_name)

print(interfaces)
info = {}
with open('show_interface.txt') as file1:
    for line_number, line in enumerate(file1, 1):
        for interface in interfaces:
            if interface in line:
                info[interface] = {'start': line_number}
            elif len(line.strip()) == 0:
                if info.get(interface) and not info[interface].get('stop'):
                    info[interface]['stop'] = line_number

print(info)

with open('show_interface.txt') as file2:
    for line_number, line in enumerate(file2, 1):
        for i in info.values():
            start, stop = i['start'], i['stop']
            if start <= line_number <= stop:
                if 'Description' in line and len(line.split()) > 1:
                    i['desc'] = line.split()[-1]
                elif 'Internet Address is' in line:
                    if not i.get("ip"):
                        i["ip"] = [line.split()[-1]]
                    else:
                        i["ip"].append(line.split()[-2])
                elif 'Hardware address is' in line:
                    i["mac"] = line.split()[-1]
                elif 'Port BW' in line:
                    i['BW'] = line.split()[2].rstrip(',')
                elif 'Rx Power' in line:
                    i['rx'] = line.split()[2].rstrip(',')
                elif 'Tx Power' in line:
                    i['tx'] = line.split()[2].rstrip(',')


from pprint import pprint
pprint(info)

with open('interface_info_done.txt', 'w') as file3:
    for key in info:
        int_name = key
        ip = '; '.join(info[key]['ip'])
        desc = info[key].get('desc', 'NA')
        bw = info[key].get("bw", "NA")
        rx = info[key].get("rx", "NA")
        tx = info[key].get("tx", "NA")
        mac = info[key].get("mac", "NA")

        file3.write(f'{int_name:20} {ip:35} {bw:5} {rx:10} {tx:10} {mac:30} {desc}\n')