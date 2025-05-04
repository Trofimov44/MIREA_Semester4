#!/bin/bash
echo "Введите путь к файлу: "
read file
if [ -f "$file" ]; then
    while IFS= read -r line; do
        echo "$line"
    done < "$file"
else
    echo "Файл не существует"
fi