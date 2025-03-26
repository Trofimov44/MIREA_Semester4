cd "$DIRECTORY" || exit

# Извлечение зависимостей
grep -rhoP '^import \K\w+' . >> imports.txt
grep -rhoP '^from \K\w+' . >> imports.txt

# Удаляем дубликаты
sort imports.txt | uniq > dependencies.txt

# Скачиваем список стандартных библиотек
wget https://raw.githubusercontent.com/pypi/stdlib-list/main/stdlib_list/lists/3.13.txt -O std_libs.txt

# Получаем список локальных модулей (имен файлов и директорий без расширений)
find . -type d -o -name "*.py" | sed 's|.*/||' | sed 's|\.py||' | sort | uniq > local_modules.txt

# Исключаем стандартные библиотеки
grep -vxFf std_libs.txt dependencies.txt > filtered_dependencies.txt

# Исключаем локальные модули
grep -vxFf local_modules.txt filtered_dependencies.txt > requirements.txt

# Очистка временных файлов
rm filtered_dependencies.txt local_modules.txt
