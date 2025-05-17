import numpy as np

# Функция для вывода симплекс-таблицы
def print_tableau(tableau, basis, non_basis):
    print("\nСимплекс-таблица:")
    header = [""] + non_basis + ["RHS"]
    print("\t".join(header))
    for i in range(len(basis)):
        row = [f"{basis[i]} ({tableau[i, 0]})"] + [f"{tableau[i, j+1]:.2f}" for j in range(tableau.shape[1]-1)]
        print("\t".join(row))
    print(basis)
    f_row = ["f"] + [f"{tableau[-1, j+1]:.2f}" for j in range(tableau.shape[1]-1)]
    print("\t".join(f_row))

# Симплекс-метод
def simplex_method():
    # Начальная симплекс-таблица
    # Переменные: x1, x2, x3, x4, x5, x6, RHS
    tableau = np.array([
        [0, 2, 3, 1, 0, 0, 0, 1000],  # x3: 2x1 + 3x2 + x3 = 1000
        [0, 2, 1, 0, 1, 0, 0, 1300],  # x4: 2x1 + x2 + x4 = 1300
        [0, 0, 3, 0, 0, 1, 0, 1500],  # x5: 3x2 + x5 = 1500
        [0, 3, 0, 0, 0, 0, 1, 1800],  # x6: 3x1 + x6 = 1800
        [0, -7, -5, 0, 0, 0, 0, 0]     # f: -7x1 - 5x2
    ], dtype=float)

    # Базисные и небазисные переменные
    basis = ["x3", "x4", "x5", "x6"]
    non_basis = ["x1", "x2", "x3", "x4", "x5", "x6"]

    iteration = 0
    while True:
        # Удаляем базисные переменные из non_basis для текущей итерации
        current_non_basis = [var for var in non_basis if var not in basis]

        print(f"\nИтерация {iteration}")
        print_tableau(tableau, basis, current_non_basis)

        # Шаг 1: Проверка на оптимальность (есть ли отрицательные элементы в f-строке)
        if np.all(tableau[-1, 1:-1] >= 0):
            print("\nОптимальное решение найдено!")
            break

        # Шаг 2: Выбор ведущего столбца (наибольший отрицательный коэффициент в f-строке)
        pivot_col = np.argmin(tableau[-1, 1:-1]) + 1
        entering_var = current_non_basis[pivot_col-1]
        print(f"Ведущий столбец: {entering_var} (индекс {pivot_col})")

        # Шаг 3: Выбор ведущей строки (минимальное положительное отношение RHS / элемент ведущего столбца)
        ratios = []
        for i in range(len(basis)):
            if tableau[i, pivot_col] > 0:
                ratios.append(tableau[i, -1] / tableau[i, pivot_col])
            else:
                ratios.append(float('inf'))
        pivot_row = np.argmin(ratios)
        if ratios[pivot_row] == float('inf'):
            print("Задача не имеет конечного решения (неограничена).")
            return

        print(f"Ведущая строка: {basis[pivot_row]} (индекс {pivot_row}), отношение = {ratios[pivot_row]:.2f}")

        # Шаг 4: Пересчет таблицы
        pivot_element = tableau[pivot_row, pivot_col]
        print(f"Разрешающий элемент: {pivot_element}")

        # Обновляем ведущую строку
        tableau[pivot_row, :] /= pivot_element

        # Обновляем остальные строки
        for i in range(tableau.shape[0]):
            if i != pivot_row:
                factor = tableau[i, pivot_col]
                tableau[i, :] -= factor * tableau[pivot_row, :]

        # Обновляем базис
        leaving_var = basis[pivot_row]
        basis[pivot_row] = entering_var
        iteration += 1

    # Извлекаем решение
    solution = {"x1": 0, "x2": 0}
    for i in range(len(basis)):
        var = basis[i]
        if var in solution:
            solution[var] = tableau[i, -1]

    print("\nРешение:")
    print(f"x1 = {solution['x1']:.2f}")
    print(f"x2 = {solution['x2']:.2f}")
    print(f"Максимальное значение целевой функции f = {tableau[-1, -1]:.2f}")

# Запускаем симплекс-метод
simplex_method()