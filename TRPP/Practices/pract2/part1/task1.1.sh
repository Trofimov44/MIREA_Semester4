#!/bin/bash
echo "Дата и время: $(date)"
echo "Зарегистрированные пользователи: $(who)"
echo "Uptime системы: $(uptime)"
echo "--------------------------------" 
echo "Дата и время: $(date)" > "task1.1.txt"
echo "Зарегистрированные пользователи: $(who)" >> task1.1.txt
echo "Uptime системы: $(uptime)" >> task1.1.txt