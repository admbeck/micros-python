from ping3 import ping

class Network:
    """Класс для пинга, или для работы с IP адресами"""
    def __init__(self, lan: str):
        net = ''
        ip_list = lan.split('.')
        for i in range(len(ip_list) - 1):
            net = net + ip_list[i] + '.'

        self.lan = net

    # def is_diapazon(self, item):
    #     return '-' in item

    def ip_separate(self, item):
        start, stop = item.split('-')
        for i in range(int(start), int(stop)+1):
            self.myping(str(i))

    def myping(self, item):
        host = self.lan + item
        resp = str(ping(host, timeout=0.1))
        if resp != 'False' and resp != 'None':
            print(f"{host} - Up")
        else:
            print(f"{host} - Down")


    def ping(self, ip='1-254'):
        """инициалтзация адресов для пинга"""
        hosts = ip.split()

        # for item in hosts:
        #     if self.is_diapazon(item):
        #         print(f"Диапазон {item}")
        #     else:
        #         print(f"Одиночный {item}")

        true_false = list(map(lambda item: '-' in item, hosts))
        true_false_ip = list(zip(true_false, hosts))

        for result, addr in true_false_ip:
            if result:
                self.ip_separate(addr)
            else:
                self.myping(addr)





ipnet = Network('192.168.8.0')
ipnet.ping('1 20 30 40-50')