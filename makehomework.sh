#!/usr/bin/env bash
# Settings
# Имя
name="Zakhidov Nodirbek"

# Script to compile python homework for micros
help="Правильное использование скрипта:\n
makehomework.sh <директория с домашней работой> <номер урока>\n
Например:
    ./makehomework.sh 2-lesson 2
Если директории пронумерованы (1-урок, 3-lesson и т.д.) то указывать номер урока не обязательно\n
ВАЖНО:
Внутрии директории с домашней работой должны быть пронумерованные .py скрипты (1-task.py, 1-execsize.py и т.д.)\n"

# Errors
err_noarg="ERROR! Укажите путь до директории.\n\n$help"
err_notdir="ERROR! Указанный параметр не является директорией.\n\n$help"
err_nopyfiles="ERROR! Нет .py файлов в директории.\n\n$help"

# Variables
dir="$1"
num="$2"
finalname=""

# Functions
getname()       # get a name for final file
{
    splitname=($name)   # turn name into array
    dirseq=${dir:0:1}   # separate 1st character from directory name
    re='^[0-9]+$'       # regex pattern to check for numbers

    if [[ $num =~ $re ]]; then
        num=$num
    elif [[ $dirseq =~ $re ]]; then
        num="$dirseq"
    else
        num="X"
    fi
    finalname="${splitname[0]}_${splitname[1]}_$num-homework.py"
}

compilehw()     # compile single document from .py files
{
    cd $dir
    files=`ls $hwdir/*.py`

    getname
    printf "$finalname\n"
    touch "$finalname"
    printf "# $name\n\n" > "$finalname"

    for file in $files; do      # write
        printf "$file\n"
        tail -n +2 "$hwdir$file" >> $finalname
        printf "\n" >> $finalname
    done
    exit
}

# main
if [ -d "$dir/homework" ]; then     # check if there are homework folders in given directory
    hwdir="$dir/homework"
elif [ -f "$dir/hw" ]; then
    hwdir="$dir/hw"
else
    hwdir="."
fi
echo $hwdir

if [ -z $dir ]; then
    printf "$err_noarg"; exit   # check if argument is given
elif [ ! -d $dir ]; then            # check if argument is a directory
    printf "$err_notdir"; exit
else
    if [ ! -f "$hwdir/*.py" ]; then     # check if .py files exist in the directory
        printf "$err_nopyfiles"; exit
    else
        compilehw
    fi
fi
