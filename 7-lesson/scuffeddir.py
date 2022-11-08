#!/usr/bin/env python3
from sys import argv
from os import listdir, path, stat
from datetime import datetime

if len(argv) > 1:
    dirname = argv[1] + "/"
else:
    dirname = "./"

files = listdir(dirname)

print(f"\nContent of directory: {dirname}\n")

headerTables = "{:20} {:7} {}"
print(headerTables.format("Date created", "Type", "Filename"))

for file in files:
    fullName = dirname + file

    fdateCreated = stat(fullName).st_ctime
    cTime = str(datetime.fromtimestamp(int(fdateCreated)))

    if path.isdir(fullName):
        print(headerTables.format(cTime, "<dir>", file))
    elif path.islink(fullName):
        print(headerTables.format(cTime, "<lnk>", file))
    elif file.endswith(".lnk"):
        print(headerTables.format(cTime, "<lnk>", file))
    else:
        print(headerTables.format(cTime, "", file))

print("-" * 20)
print(f"# of objects: {len(files)}")
