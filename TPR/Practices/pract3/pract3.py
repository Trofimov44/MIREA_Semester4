import pandas as pd

# Установить формат отображения чисел
pd.options.display.float_format = '{:.2f}'.format

# Альтернативы
alternatives = [
    {'name': '1. Сарафаново', 'price': 129, 'weight': 970, 'calories': 46, 'shelf_life': 180},
    {'name': '2. Простоквашино', 'price': 99, 'weight': 930, 'calories': 53, 'shelf_life': 16},
    {'name': '3. Просто', 'price': 85, 'weight': 970, 'calories': 53, 'shelf_life': 180},
    {'name': '4. Искренне ваш', 'price': 85, 'weight': 930, 'calories': 53, 'shelf_life': 16},
    {'name': '5. Зелёная линия', 'price': 79, 'weight': 900, 'calories': 40, 'shelf_life': 10},
]
    
df = pd.DataFrame(alternatives)
df.index = df.index + 1 
print(df, '\n')

# Таблица критериев
criteria_data = {
    'К1': [1, 1, 1/3, 1/5],
    'К2': [1, 1, 1/3, 1/5],
    'К3': [3, 3, 1, 1/3],
    'К4': [5, 5, 3, 1]
}
criteria_df = pd.DataFrame(criteria_data, index=['К1', 'К2', 'К3', 'К4'], dtype=float)  # Преобразование в float
print("Таблица критериев:")
print(criteria_df, '\n')

# Вычисление суммы каждой строки и вывод
print("Вычисление V:")
row_products = criteria_df.prod(axis=1)  # Произведение элементов в строке
row_roots = row_products ** (1 / len(criteria_df.columns))  # Корень степени n
for i, value in enumerate(row_roots, start=1):
    print(f"V{i} = ({'x'.join(map(str, criteria_df.iloc[i-1]))})^(1/{len(criteria_df.columns)}) = {value:.3f};")
# Вычисление суммы всех V и вывод W
sum_v = row_roots.sum()
print(f"ΣVi = {' + '.join(f'{v:.3f}' for v in row_roots)} = {sum_v:.3f}\n")

print("Вычисление W2i:")
for i, value in enumerate(row_roots, start=1):
    w = value / sum_v
    print(f"W2{i} = {value:.3f} / {sum_v:.3f} = {w:.3f};")

# Вычисление W2i и вывод в формате (0.388; 0.388; 0.150; 0.075;)
w_values = [f"{value / sum_v:.3f}" for value in row_roots]
print(f"W2i = ({'; '.join(w_values)});\n")

# Таблица сравнения по критерию K1
k1_data = {
    'A1': [1, 1/5, 1/7, 1/7, 1/9],
    'A2': [5, 1, 1/5, 1/5, 1/7],
    'A3': [7, 5, 1, 1, 1/3],
    'A4': [7, 5, 1, 1, 1/3],
    'A5': [9, 7, 3, 3, 1]
}

k1_df = pd.DataFrame.from_dict(k1_data, orient='index', dtype=float, columns=['A1', 'A2', 'A3', 'A4', 'A5'])
print("Таблица сравнения по критерию K1:")
print(k1_df, '\n')

# Вычисление V_{K1i}
print("Вычисление V_K1i:")
k1_row_products = k1_df.prod(axis=1)  # Произведение элементов в строке
k1_row_roots = k1_row_products ** (1 / len(k1_df.columns))  # Корень степени n
for i, value in enumerate(k1_row_roots, start=1):
    print(f"V_K1{i} = ({'x'.join(map(str, k1_df.iloc[i-1]))})^(1/{len(k1_df.columns)}) = {value:.3f};")

# Вычисление суммы всех V_{K1i} и вывод W_{K1i}
k1_sum_v = k1_row_roots.sum()
print(f"ΣV_K1i = {' + '.join(f'{v:.3f}' for v in k1_row_roots)} = {k1_sum_v:.3f}\n")

print("Вычисление W_K1i:")
for i, value in enumerate(k1_row_roots, start=1):
    w = value / k1_sum_v
    print(f"W_K1{i} = {value:.3f} / {k1_sum_v:.3f} = {w:.3f};")

# Вывод W_{K1i} в формате (0.388; 0.388; 0.150; 0.075;)
k1_w_values = [f"{value / k1_sum_v:.3f}" for value in k1_row_roots]
print(f"W_K1i = ({'; '.join(k1_w_values)});\n")

# Таблица сравнения по критерию K2
k2_data = {
    'A1': [1, 5, 1, 5, 7],
    'A2': [1/5, 1, 1/5, 1, 3],
    'A3': [1, 5, 1, 5, 7],
    'A4': [1/5, 1, 1/5, 1, 3],
    'A5': [1/7, 1/3, 1/7, 1/3, 1]
}

k2_df = pd.DataFrame.from_dict(k2_data, orient='index', dtype=float, columns=['A1', 'A2', 'A3', 'A4', 'A5'])
print("Таблица сравнения по критерию K2:")
print(k2_df, '\n')

# Вычисление V_{K2i}
print("Вычисление V_K2i:")
k2_row_products = k2_df.prod(axis=1)  # Произведение элементов в строке
k2_row_roots = k2_row_products ** (1 / len(k2_df.columns))  # Корень степени n
for i, value in enumerate(k2_row_roots, start=1):
    print(f"V_K2{i} = ({'x'.join(map(str, k2_df.iloc[i-1]))})^(1/{len(k2_df.columns)}) = {value:.3f};")

# Вычисление суммы всех V_{K2i} и вывод W_{K2i}
k2_sum_v = k2_row_roots.sum()
print(f"ΣV_K2i = {' + '.join(f'{v:.3f}' for v in k2_row_roots)} = {k2_sum_v:.3f}\n")

print("Вычисление W_K2i:")
for i, value in enumerate(k2_row_roots, start=1):
    w = value / k2_sum_v
    print(f"W_K2{i} = {value:.3f} / {k2_sum_v:.3f} = {w:.3f};")

# Вывод W_{K2i} в формате (0.388; 0.388; 0.150; 0.075;)
k2_w_values = [f"{value / k2_sum_v:.3f}" for value in k2_row_roots]
print(f"W_K2i = ({'; '.join(k2_w_values)});\n")

# Таблица сравнения по критерию K3
k3_data = {
    'A1': [1, 5, 5, 5, 1/3],
    'A2': [1/5, 1, 1, 1, 1/7],
    'A3': [1/5, 1, 1, 1, 1/7],
    'A4': [1/5, 1, 1, 1, 1/7],
    'A5': [3, 7, 7, 7, 1]
}

k3_df = pd.DataFrame.from_dict(k3_data, orient='index', dtype=float, columns=['A1', 'A2', 'A3', 'A4', 'A5'])
print("Таблица сравнения по критерию K3:")
print(k3_df, '\n')

# Вычисление V_{K3i}
print("Вычисление V_K3i:")
k3_row_products = k3_df.prod(axis=1)  # Произведение элементов в строке
k3_row_roots = k3_row_products ** (1 / len(k3_df.columns))  # Корень степени n
for i, value in enumerate(k3_row_roots, start=1):
    print(f"V_K3{i} = ({'x'.join(map(str, k3_df.iloc[i-1]))})^(1/{len(k3_df.columns)}) = {value:.3f};")

# Вычисление суммы всех V_{K3i} и вывод W_{K3i}
k3_sum_v = k3_row_roots.sum()
print(f"ΣV_K3i = {' + '.join(f'{v:.3f}' for v in k3_row_roots)} = {k3_sum_v:.3f}\n")

print("Вычисление W_K3i:")
for i, value in enumerate(k3_row_roots, start=1):
    w = value / k3_sum_v
    print(f"W_K3{i} = {value:.3f} / {k3_sum_v:.3f} = {w:.3f};")

# Вывод W_{K3i} в формате (0.388; 0.388; 0.150; 0.075;)
k3_w_values = [f"{value / k3_sum_v:.3f}" for value in k3_row_roots]
print(f"W_K3i = ({'; '.join(k3_w_values)});\n")

# Таблица сравнения по критерию K4
k4_data = {
    'A1': [1, 9, 1, 9, 9],
    'A2': [1/9, 1, 1/9, 1, 5],
    'A3': [1, 9, 1, 9, 9],
    'A4': [1/9, 1, 1/9, 1, 5],
    'A5': [1/9, 1/5, 1/9, 1/5, 1]
}

k4_df = pd.DataFrame.from_dict(k4_data, orient='index', dtype=float, columns=['A1', 'A2', 'A3', 'A4', 'A5'])
print("Таблица сравнения по критерию K4:")
print(k4_df, '\n')

# Вычисление V_{K4i}
print("Вычисление V_K4i:")
k4_row_products = k4_df.prod(axis=1)  # Произведение элементов в строке
k4_row_roots = k4_row_products ** (1 / len(k4_df.columns))  # Корень степени n
for i, value in enumerate(k4_row_roots, start=1):
    print(f"V_K4{i} = ({'x'.join(map(str, k4_df.iloc[i-1]))})^(1/{len(k4_df.columns)}) = {value:.3f};")

# Вычисление суммы всех V_{K4i} и вывод W_{K4i}
k4_sum_v = k4_row_roots.sum()
print(f"ΣV_K4i = {' + '.join(f'{v:.3f}' for v in k4_row_roots)} = {k4_sum_v:.3f}\n")

print("Вычисление W_K4i:")
for i, value in enumerate(k4_row_roots, start=1):
    w = value / k4_sum_v
    print(f"W_K4{i} = {value:.3f} / {k4_sum_v:.3f} = {w:.3f};")

# Вывод W_{K4i}
k4_w_values = [f"{value / k4_sum_v:.3f}" for value in k4_row_roots]
print(f"W_K4i = ({'; '.join(k4_w_values)});\n")


# Вычисление и вывод сумм столбцов (Si) для таблицы критериев
print("Вычисление сумм столбцов критериев:")
for i, col in enumerate(criteria_df.columns, start=1):
    column_sum = criteria_df[col].sum()
    elements = ' + '.join([f"{x:.3f}".rstrip('0').rstrip('.') if isinstance(x, float) else str(x) for x in criteria_df[col]])
    print(f"S_{i} = {elements} = {column_sum:.3f};")

# Вычисление и вывод P_i = S_i * W2i
print("\nВычисление P_i:")
for i, (s, w) in enumerate(zip(criteria_df.sum(), row_roots / sum_v), start=1):
    p = s * w
    print(f"P_{i} = S_{i} × W2{i} = {s:.3f} × {w:.3f} = {p:.2f};")

# Вычисление λ_max, ИС и ОС
n = 4  # Количество критериев
SI = 0.90  # Средний индекс согласованности для n=4

# Сумма P_i (λ_max)
lambda_max = sum([s * w for s, w in zip(criteria_df.sum(), row_roots / sum_v)])
print(f"\nλ_max = P_1 + P_2 + P_3 + P_4 = {lambda_max:.2f}.")

# Индекс согласованности (ИС)
IC = (lambda_max - n) / (n - 1)
print(f"ИС = (λ_max - n)/(n - 1) = ({lambda_max:.2f} - {n})/({n} - 1) = {IC:.4f}.")

# Отношение согласованности (ОС)
OC = IC / SI
print(f"ОС = ИС/СИ = {IC:.4f}/{SI} = {OC:.3f}.")

# Проверка согласованности
if OC <= 0.10:
    print("Значение ОС меньше или равно 0.10 → матрица согласована.")
else:
    print("Значение ОС превышает 0.10 → требуется пересмотр матрицы.")

# --- Расчёты для K1 ---
n_k1 = 5  # Количество альтернатив
SI_k1 = 1.12  # СИ для n=5

# 1. Суммы столбцов Sᵢ для K1
print("\nВычисление сумм столбцов для K1:")
S_k1 = k1_df.sum()
for i, s in enumerate(S_k1, start=1):
    print(f"S_K1_{i} = {' + '.join(f'{x:.3f}'.rstrip('0').rstrip('.') for x in k1_df[f'A{i}'])} = {s:.3f};")

# 2. Pᵢ = Sᵢ × W_K1i
print("\nВычисление P_K1i:")
P_k1 = S_k1 * (k1_row_roots / k1_sum_v)
for i, (s, w, p) in enumerate(zip(S_k1, k1_row_roots / k1_sum_v, P_k1), start=1):
    print(f"P_K1_{i} = S_K1_{i} × W_K1_{i} = {s:.3f} × {w:.3f} = {p:.2f};")

# 3. λ_max, ИС, ОС
lambda_max_k1 = P_k1.sum()
IC_k1 = (lambda_max_k1 - n_k1) / (n_k1 - 1)
OC_k1 = IC_k1 / SI_k1

print(f"\nλ_max_K1 = P_K1_1 + P_K1_2 + P_K1_3 + P_K1_4 + P_K1_5 = {lambda_max_k1:.2f}.")
print(f"ИС_K1 = (λ_max_K1 - n)/(n - 1) = ({lambda_max_k1:.2f} - {n_k1})/({n_k1} - 1) = {IC_k1:.4f}.")
print(f"ОС_K1 = ИС_K1/СИ = {IC_k1:.4f}/{SI_k1} = {OC_k1:.3f}.")

if OC_k1 <= 0.10:
    print("ОС_K1 ≤ 0.10 → матрица K1 согласована.")
else:
    print("ОС_K1 > 0.10 → требуется пересмотр матрицы K1.")

# --- Расчёты для K2 ---
n_k2 = 5  # Количество альтернатив
SI_k2 = 1.12  # СИ для n=5

# 1. Суммы столбцов Sᵢ для K2
print("\nВычисление сумм столбцов для K2:")
S_k2 = k2_df.sum()
for i, s in enumerate(S_k2, start=1):
    print(f"S_K2_{i} = {' + '.join(f'{x:.3f}'.rstrip('0').rstrip('.') for x in k2_df[f'A{i}'])} = {s:.3f};")

# 2. Pᵢ = Sᵢ × W_K2i
print("\nВычисление P_K2i:")
P_k2 = S_k2 * (k2_row_roots / k2_sum_v)
for i, (s, w, p) in enumerate(zip(S_k2, k2_row_roots / k2_sum_v, P_k2), start=1):
    print(f"P_K2_{i} = S_K2_{i} × W_K2_{i} = {s:.3f} × {w:.3f} = {p:.2f};")

# 3. λ_max, ИС, ОС
lambda_max_k2 = P_k2.sum()
IC_k2 = (lambda_max_k2 - n_k2) / (n_k2 - 1)
OC_k2 = IC_k2 / SI_k2

print(f"\nλ_max_K2 = P_K2_1 + P_K2_2 + P_K2_3 + P_K2_4 + P_K2_5 = {lambda_max_k2:.2f}.")
print(f"ИС_K2 = (λ_max_K2 - n)/(n - 1) = ({lambda_max_k2:.2f} - {n_k2})/({n_k2} - 1) = {IC_k2:.4f}.")
print(f"ОС_K2 = ИС_K2/СИ = {IC_k2:.4f}/{SI_k2} = {OC_k2:.3f}.")

if OC_k2 <= 0.10:
    print("ОС_K2 ≤ 0.10 → матрица K2 согласована.")
else:
    print("ОС_K2 > 0.10 → требуется пересмотр матрицы K2.")


# --- Расчёты для K3 ---
n_k3 = 5  # Количество альтернатив
SI_k3 = 1.12  # СИ для n=5

# 1. Суммы столбцов Sᵢ для K3
print("\nВычисление сумм столбцов для K3:")
S_k3 = k3_df.sum()
for i, s in enumerate(S_k3, start=1):
    print(f"S_K3_{i} = {' + '.join(f'{x:.3f}'.rstrip('0').rstrip('.') for x in k3_df[f'A{i}'])} = {s:.3f};")

# 2. Pᵢ = Sᵢ × W_K3i
print("\nВычисление P_K3i:")
P_k3 = S_k3 * (k3_row_roots / k3_sum_v)
for i, (s, w, p) in enumerate(zip(S_k3, k3_row_roots / k3_sum_v, P_k3), start=1):
    print(f"P_K3_{i} = S_K3_{i} × W_K3_{i} = {s:.3f} × {w:.3f} = {p:.2f};")

# 3. λ_max, ИС, ОС
lambda_max_k3 = P_k3.sum()
IC_k3 = (lambda_max_k3 - n_k3) / (n_k3 - 1)
OC_k3 = IC_k3 / SI_k3

print(f"\nλ_max_K3 = P_K3_1 + P_K3_2 + P_K3_3 + P_K3_4 + P_K3_5 = {lambda_max_k3:.2f}.")
print(f"ИС_K3 = (λ_max_K3 - n)/(n - 1) = ({lambda_max_k3:.2f} - {n_k3})/({n_k3} - 1) = {IC_k3:.4f}.")
print(f"ОС_K3 = ИС_K3/СИ = {IC_k3:.4f}/{SI_k3} = {OC_k3:.3f}.")

if OC_k3 <= 0.10:
    print("ОС_K3 ≤ 0.10 → матрица K3 согласована.")
else:
    print("ОС_K3 > 0.10 → требуется пересмотр матрицы K3.")

# --- Расчёты для K4 ---
n_k4 = 5  # Количество альтернатив
SI_k4 = 1.12  # СИ для n=5

# 1. Суммы столбцов Sᵢ для K4
print("\nВычисление сумм столбцов для K4:")
S_k4 = k4_df.sum()
for i, s in enumerate(S_k4, start=1):
    print(f"S_K4_{i} = {' + '.join(f'{x:.3f}'.rstrip('0').rstrip('.') for x in k4_df[f'A{i}'])} = {s:.3f};")

# 2. Pᵢ = Sᵢ × W_K4i
print("\nВычисление P_K4i:")
P_k4 = S_k4 * (k4_row_roots / k4_sum_v)
for i, (s, w, p) in enumerate(zip(S_k4, k4_row_roots / k4_sum_v, P_k4), start=1):
    print(f"P_K4_{i} = S_K4_{i} × W_K4_{i} = {s:.3f} × {w:.3f} = {p:.2f};")

# 3. λ_max, ИС, ОС
lambda_max_k4 = P_k4.sum()
IC_k4 = (lambda_max_k4 - n_k4) / (n_k4 - 1)
OC_k4 = IC_k4 / SI_k4

print(f"\nλ_max_K4 = P_K4_1 + P_K4_2 + P_K4_3 + P_K4_4 + P_K4_5 = {lambda_max_k4:.2f}.")
print(f"ИС_K4 = (λ_max_K4 - n)/(n - 1) = ({lambda_max_k4:.2f} - {n_k4})/({n_k4} - 1) = {IC_k4:.4f}.")
print(f"ОС_K4 = ИС_K4/СИ = {IC_k4:.4f}/{SI_k4} = {OC_k4:.3f}.")

if OC_k4 <= 0.10:
    print("ОС_K4 ≤ 0.10 → матрица K4 согласована.")
else:
    print("ОС_K4 > 0.10 → требуется пересмотр матрицы K4.")

# Вывод всех W
print("\nИтоговые значения W:")
print(f"W2i = ({'; '.join(w_values)});")
print(f"W3K1Y = ({'; '.join(k1_w_values)});")
print(f"W3K2Y = ({'; '.join(k2_w_values)});")
print(f"W3K3Y = ({'; '.join(k3_w_values)});")
print(f"W3K4Y = ({'; '.join(k4_w_values)});")

# Рассчет W1, W2, W3, W4, W5
print("\nРассчет W1, W2, W3, W4, W5:")

# Преобразование строковых значений W в числовые
W2i = list(map(float, w_values))
W3K1Y = list(map(float, k1_w_values))
W3K2Y = list(map(float, k2_w_values))
W3K3Y = list(map(float, k3_w_values))
W3K4Y = list(map(float, k4_w_values))

# Формулы для W1, W2, W3, W4, W5
W1 = sum(W2i[j] * W for j, W in enumerate([W3K1Y[0], W3K2Y[0], W3K3Y[0], W3K4Y[0]]))
W2 = sum(W2i[j] * W for j, W in enumerate([W3K1Y[1], W3K2Y[1], W3K3Y[1], W3K4Y[1]]))
W3 = sum(W2i[j] * W for j, W in enumerate([W3K1Y[2], W3K2Y[2], W3K3Y[2], W3K4Y[2]]))
W4 = sum(W2i[j] * W for j, W in enumerate([W3K1Y[3], W3K2Y[3], W3K3Y[3], W3K4Y[3]]))
W5 = sum(W2i[j] * W for j, W in enumerate([W3K1Y[4], W3K2Y[4], W3K3Y[4], W3K4Y[4]]))

# Вывод результатов
print(f"W1 = {' + '.join([f'{W2i[j]:.3f} × {W:.3f}' for j, W in enumerate([W3K1Y[0], W3K2Y[0], W3K3Y[0], W3K4Y[0]])])} = {W1:.3f}")
print(f"W2 = {' + '.join([f'{W2i[j]:.3f} × {W:.3f}' for j, W in enumerate([W3K1Y[1], W3K2Y[1], W3K3Y[1], W3K4Y[1]])])} = {W2:.3f}")
print(f"W3 = {' + '.join([f'{W2i[j]:.3f} × {W:.3f}' for j, W in enumerate([W3K1Y[2], W3K2Y[2], W3K3Y[2], W3K4Y[2]])])} = {W3:.3f}")
print(f"W4 = {' + '.join([f'{W2i[j]:.3f} × {W:.3f}' for j, W in enumerate([W3K1Y[3], W3K2Y[3], W3K3Y[3], W3K4Y[3]])])} = {W4:.3f}")
print(f"W5 = {' + '.join([f'{W2i[j]:.3f} × {W:.3f}' for j, W in enumerate([W3K1Y[4], W3K2Y[4], W3K3Y[4], W3K4Y[4]])])} = {W5:.3f}")

# Приоритеты альтернатив
print("\nПриоритеты альтернатив:")
alternatives_names = [alt['name'] for alt in alternatives]
for i, W in enumerate([W1, W2, W3, W4, W5], start=1):
    print(f"Альтернатива {alternatives_names[i-1]} - W{i} приоритет равен {W:.3f}")

# Определение лучшей альтернативы
best_index = max(range(len([W1, W2, W3, W4, W5])), key=lambda i: [W1, W2, W3, W4, W5][i])
best_alternative = alternatives_names[best_index]
print(f"\nЛучшая альтернатива: {best_alternative} с W = {[W1, W2, W3, W4, W5][best_index]:.3f}")
