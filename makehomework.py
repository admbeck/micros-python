#!/usr/bin/env python3
"""
File: makehomework.py
Author: Zakhidov Beck
Email: admbeck@outlook.com
Github: https://github.com/admbeck
Description: A script to compile homeworks for micros lessons
"""
import os
import sys
import re


def helpPage():
    """Help page"""
    print("""Usage: ./makehomework.py [FOLDER]...
Compile ordered homeowork files into a single file.

You can create a .credentials file to store name and surname
Folder name should start with a number and homework files should be numbered in order.""")

def order(x):
    """Soring function"""
    return int(re.search("\d+", x).group(0))

def err(reason):
    """Temporary error function"""
    errorDict = {
        'nohomework': 'No homework folder found in the given directory. Aborting.'
    }
    sys.exit(errorDict[reason])
    # TODO:
    # make proper exceptions

def checkCreds():
    """Checks for credentials"""
    creds = './.credentials'

    if os.path.isfile(creds):
        with open(creds, encoding="UTF-8") as file:
            name = file.readline()
    else:
        name = input("Input your name: ")
    return name

def compileFile(listfile, dir):
    """Compile complete homework file"""
    name = checkCreds()

    with open(f"{dir.rsplit('/', 1)[0]}/{hwFilename(name, dir)}", "w", encoding="UTF-8") as compfile:
        compfile.write(f"# {name}")
        counter = 1
        for i in listfile:
            with open(f"{dir}/{i}", encoding="UTF-8") as file:
                for k in file:
                    if not k.startswith("#!"):
                        compfile.write(k)
            if counter != len(listfile):
                compfile.write("\n")
                counter += 1

def hwFilename(name, dir):
    scoreName = name.replace(" ", "_").replace("\n", "")
    count = re.search("\d+", dir).group(0)
    return f"{scoreName}_{count}-homework.py"

def main():
    if str(sys.argv[1]) == "--help":
        helpPage()

    if len(sys.argv) != 2:
        helpPage()

    origDir = sys.argv[1]

    if "homework" in os.listdir(origDir):
        hwDir = f"{origDir}/homework"
    else:
        err('nohomework')

    hwFiles = os.listdir(hwDir)
    hwFiles.sort(key=order)

    compileFile(hwFiles, hwDir)


if __name__ == '__main__':
    main()
