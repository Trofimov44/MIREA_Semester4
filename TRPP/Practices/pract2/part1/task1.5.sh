#!/bin/bash
echo "Введите путь к директории: "
read directory

if [ -d "$directory" ]; then
    echo "Объем директории $directory:"
    ls -lR "$directory" | awk '{total += $5} END {print total/1024/1024 " MB"}'
else
    echo "Директория $directory не существует"
fi