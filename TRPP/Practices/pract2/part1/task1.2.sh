#!/bin/bash
echo "Введите путь к каталогу: "
read directory
if [ -d "$directory" ]; then
    echo "Содержимое каталога $directory:"
    ls -l "$directory"
else
    echo "Каталог $directory не существует"
fi