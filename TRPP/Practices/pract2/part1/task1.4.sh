#!/bin/bash
for item in *; do
    if [ -f "$item" ]; then
        echo "$item - файл"
    elif [ -d "$item" ]; then
        echo "$item - директория"
    fi
done