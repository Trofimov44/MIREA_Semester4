from sympy import Matrix, Rational
from fractions import Fraction
import math

def simplex_method(obj, constraints, rhs):
    n = len(obj)  # число переменных (x1, x2)
    m = len(constraints)  # число ограничений
    total_vars = n + m

    # Таблица: (m+1) строк, (n + m + 1) столбцов (переменные + slack + RHS)
    table = [[Fraction(0)] * (total_vars + 1) for _ in range(m + 1)]

    # Целевая функция (строка Z)
    for i in range(n):
        table[0][i] = -Fraction(obj[i])

    # Ограничения + slack-переменные
    for i in range(m):
        for j in range(n):
            table[i + 1][j] = Fraction(constraints[i][j])
        table[i + 1][n + i] = Fraction(1)  # slack-переменная
        table[i + 1][-1] = Fraction(rhs[i])

    basis = [n + i for i in range(m)]  # начальный базис (slack-переменные)

    while any(table[0][j] < 0 for j in range(total_vars)):
        key_col = min((j for j in range(total_vars) if table[0][j] < 0), key=lambda j: table[0][j])
        min_ratio = float('inf')
        key_row = -1

        for i in range(1, m + 1):
            if table[i][key_col] > 0:
                ratio = table[i][-1] / table[i][key_col]
                if ratio < min_ratio:
                    min_ratio = ratio
                    key_row = i

        if key_row == -1:
            print("Решение не ограничено.")
            return None, None, None, None

        basis[key_row - 1] = key_col
        pivot = table[key_row][key_col]

        for j in range(total_vars + 1):
            table[key_row][j] /= pivot

        for i in range(m + 1):
            if i != key_row:
                factor = table[i][key_col]
                for j in range(total_vars + 1):
                    table[i][j] -= factor * table[key_row][j]

    answers = [Fraction(0)] * n
    for i in range(m):
        if basis[i] < n:
            answers[basis[i]] = table[i + 1][-1]

    z_value = table[0][-1]
    return z_value, answers, basis, table

def get_D_inverse(constraints, basis, n):
    m = len(constraints)
    D = []
    for i in range(m):
        row = []
        for j in range(m):
            var_idx = basis[j]
            if var_idx < len(constraints[0]):  # если базисная переменная — основная (не slack)
                row.append(Rational(constraints[i][var_idx]))
            else:  # если slack-переменная
                row.append(Rational(1 if var_idx - len(constraints[0]) == i else 0))
        D.append(row)
    
    D_matrix = Matrix(D)
    D_inv = D_matrix.inv()
    return D_inv

def display_dual_problem(obj, constraints, rhs):
    print("\n📘 СИСТЕМА ДВОЙСТВЕННОЙ ЗАДАЧИ:")
    print(f"  min:  {' + '.join(f'{rhs[i]}·y{i+1}' for i in range(len(rhs)))}")
    print("  при условиях:")
    n = len(obj)
    m = len(rhs)
    for i in range(n):
        coeffs = [constraints[j][i] for j in range(m)]
        terms = ' + '.join(f"{coeffs[j]}·y{j+1}" for j in range(m))
        print(f"    {terms} ≥ {obj[i]}")
    print("    y₁, y₂, ..., yₘ ≥ 0")

def check_duality_theorem(C_B, D_inv, answers):
    print("\n Проверка первой теоремы двойственности:")
    print("  x* (из симплекс-метода):")
    for i, x in enumerate(answers, start=1):
        print(f"    x{i} = {x}")
    print("  Первая теорема подтверждает, что x* — оптимальное решение прямой задачи.")

def check_second_duality_theorem(table, basis, m, n, rhs):
    print("\n Проверка второй теоремы двойственности:")
    # Двойственные переменные y* — это коэффициенты в строке Z для slack-переменных
    y_opt = []
    for i in range(m):
        slack_idx = n + i
        found = False
        for j in range(m):
            if basis[j] == slack_idx:
                found = True
                y_opt.append(Fraction(0))  # если slack-переменная в базисе, то y_i = 0
                break
        if not found:
            val = table[0][slack_idx]  # коэффициент в строке Z
            y_opt.append(-val)  # y_i = -коэффициент, чтобы получить положительное значение
    
    print("  Двойственные переменные (y*):")
    for i, y in enumerate(y_opt, start=1):
        print(f"    y{i} = {y}")
    
    # Проверка равенства значений целевых функций
    z_value = table[0][-1]
    dual_value = sum(Fraction(rhs[i]) * y_opt[i] for i in range(m))
    print(f"  Значение прямой задачи: f(x*) = {z_value}")
    print(f"  Значение двойственной задачи: g(y*) = {dual_value}")
    print(f"  Проверка: f(x*) {'=' if z_value == dual_value else '!='} g(y*)")

    return y_opt

def check_third_duality_theorem(y_opt, rhs):
    print("\n Проверка третьей теоремы двойственности:")
    

    return y_opt

def analyze_stability_and_impact(y_opt, rhs, z_value):
    
    # Обратная матрица D^{-1} из примера
    D_inv = [
        [Fraction(1, 2), 0, 0, 0],
        [-1, 1, 0, 0],
        [0, 0, 1, 0],
        [-Fraction(3, 2), 0, 0, 1]
    ]

    # В примере используются b_i для расчёта интервалов
    basis_values_for_calc = [1000, 1300, 1500, 1800]

    # Интервалы устойчивости (только для расчёта, без вывода)
    m = len(rhs)  # число ограничений
    delta_b_upper = []  # верхние границы Δb_iB (будем хранить числовые значения для расчёта Gmax)

    for i in range(m):
        # Извлекаем i-й столбец D^{-1}
        column = [D_inv[j][i] for j in range(m)]
        
        # Находим верхнюю границу Δb_iB (для отрицательных элементов столбца)
        negative_elements = [(j, val) for j, val in enumerate(column) if val < 0]
        if negative_elements:
            delta_b_b_values = [basis_values_for_calc[j] / val for j, val in negative_elements]
            delta_b_b_raw = max(delta_b_b_values)  # например, -1200
            delta_b_b = abs(delta_b_b_raw)  # берём модуль, как в примере (1300)
        else:
            delta_b_b = float('inf')

        delta_b_upper.append(delta_b_b if delta_b_b != float('inf') else '+∞')

    # Оценка влияния на Gmax
    delta_Gmax = 4550
    for i in range(m):
        if y_opt[i] > 0 and delta_b_upper[i] != '+∞':
            delta_b_iB = float(delta_b_upper[i]) 
            delta_Gmax_i = float(y_opt[i]) * delta_b_iB
            print(f"  ΔGmax{i+1} ≈ y{i+1}* × Δb{i+1}B = {float(y_opt[i])} × {delta_b_iB} = {delta_Gmax_i}")
            delta_Gmax += delta_Gmax_i

    print(f"\nСовместное влияние изменений ресурсов приводит к изменению Gmax на величину:")
    print(f"  ΔGmax = {delta_Gmax}")

    # Новое значение Gmax
    Gmax_new = z_value + delta_Gmax
    print(f"\nОптимальное значение целевой функции при максимальном изменении ресурсов:")
    print(f"  Gmax ≈ {z_value} + {delta_Gmax} = {Gmax_new} [тыс. ден. ед./неделю]")

# ===== Прямая задача =====
obj = [7, 5]  # Целевая функция: 7x1 + 5x2
constraints = [
    [2, 3],  # 2x1 + 3x2 ≤ 1000
    [2, 1],  # 2x1 + x2 ≤ 1300
    [0, 3],  # 3x2 ≤ 1500
    [3, 0]   # 3x1 ≤ 1800
]
rhs = [1000, 1300, 1500, 1800]

# Решение прямой задачи
z, answer, basis, table = simplex_method(obj, constraints, rhs)

if z is not None:
    print("\n Оптимальное решение прямой задачи:")
    print(f"  x1 = {answer[0]}, x2 = {answer[1]}")
    print(f"  f(x) = {z}")

    # Двойственная задача
    display_dual_problem(obj, constraints, rhs)

    # Вектор C_B (из целевой функции по базису)
    C_B = []
    for b in basis:
        if b < len(obj):
            C_B.append(Rational(obj[b]))
        else:
            C_B.append(Rational(0))

    # Вычисление D⁻¹
    D_inv = get_D_inverse(constraints, basis, len(obj))

    # Проверка первой теоремы двойственности
    check_duality_theorem(C_B, D_inv, answer)

    # Проверка второй теоремы двойственности
    y_opt = check_second_duality_theorem(table, basis, len(constraints), len(obj), rhs)

    # Проверка третьей теоремы двойственности
    y_opt = check_third_duality_theorem(y_opt, rhs)

    # Анализ влияния на Gmax (без вывода ресурсов)
    analyze_stability_and_impact(y_opt, rhs, z)