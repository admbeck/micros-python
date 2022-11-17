#!/usr/bin/env python3
from ping3 import ping
import sys

def ipSeparate(var):
    min, max = var.split('-')
    for i in range(int(min), int(max)+1):
        myPing(str(i))


def myPing(lastOctet):
    lan = '192.168.8.'
    host = lan + lastOctet
    resp = str(ping(host, timeout=0.1))

    if resp != 'False' and resp != 'None':
        print(f"{host:16} - UP")
    else:
        print(f"{host:16} - DOWN")


def main():
    askUser = input("Дай IP адреса: ").split()
    trueFalse = list(map(lambda item: '-' in item, askUser))
    trueFalseIp = list(zip(trueFalse, askUser))

    # trueFalse = list(map(lambda item: '-' in item, sys.argv[1:]))
    # trueFalseIp = list(zip(trueFalse, sys.argv[1:]))

    for key, value in trueFalseIp:
        if key:
            ipSeparate(value)
        else:
            myPing(value)


if __name__ == '__main__':
    main()
