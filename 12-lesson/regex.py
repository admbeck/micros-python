#!/usr/bin/env python3
import re

with open('registrations.txt', encoding="UTF-8") as regist:
    good = open('good.txt', mode='w', encoding="UTF-8")
    bad = open('bad.txt', mode='w', encoding="UTF-8")

    regex = "\S+ \w+@\w+.\S+ [0-9]{2}$"
    for line in regist:
        if (len(line.split()) == 3):
            goodEmail = re.search(regex, line)
            good.write(line)
        else:
            bad.write(line)
