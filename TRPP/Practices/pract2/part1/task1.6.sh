#!/bin/bash
echo "Введите путь к директории: "
read directory
if [ -d "$directory" ]
then
    echo "Исполняемые файлы в $directory:"
    find "$directory" -type f -executable -print
else
    echo "Директория не существует"
fi