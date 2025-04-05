import pandas as pd

# Установка формата отображения чисел
pd.options.display.float_format = '{:.2f}'.format

def create_dataframe(data, index=None, columns=None, orient=None):
    """Создает DataFrame с указанными данными и индексами/столбцами"""
    if orient == 'index':
        return pd.DataFrame.from_dict(data, orient='index', columns=columns, dtype=float)
    return pd.DataFrame(data, index=index, columns=columns, dtype=float)

def calculate_weights(df, prefix=''):
    """Вычисляет веса для матрицы сравнений"""
    # Вычисление V
    row_products = df.prod(axis=1)
    row_roots = row_products ** (1 / len(df.columns))
    
    print(f"\nВычисление V_{prefix}:")
    for i, value in enumerate(row_roots, start=1):
        print(f"V_{prefix}{i} = ({'x'.join(map(str, df.iloc[i-1]))})^(1/{len(df.columns)}) = {value:.3f};")
    
    # Вычисление W
    sum_v = row_roots.sum()
    print(f"ΣV_{prefix}i = {' + '.join(f'{v:.3f}' for v in row_roots)} = {sum_v:.3f}")
    
    print(f"\nВычисление W_{prefix}i:")
    w_values = []
    for i, value in enumerate(row_roots, start=1):
        w = value / sum_v
        w_values.append(w)
        print(f"W_{prefix}{i} = {value:.3f} / {sum_v:.3f} = {w:.3f};")
    
    print(f"W_{prefix}i = ({'; '.join(f'{w:.3f}' for w in w_values)});")
    return w_values, row_roots, sum_v

def calculate_consistency(P_values, n, SI, prefix=''):
    """Вычисляет согласованность матрицы"""
    lambda_max = sum(P_values)
    IC = (lambda_max - n) / (n - 1)
    OC = IC / SI
    
    print(f"\nλ_max_{prefix} = {' + '.join(f'P_{prefix}{i}' for i in range(1, n+1))} = {lambda_max:.2f}.")
    print(f"ИС_{prefix} = (λ_max_{prefix} - n)/(n - 1) = ({lambda_max:.2f} - {n})/({n} - 1) = {IC:.4f}.")
    print(f"ОС_{prefix} = ИС_{prefix}/СИ = {IC:.4f}/{SI} = {OC:.3f}.")
    
    if OC <= 0.10:
        print(f"ОС_{prefix} ≤ 0.10 → матрица {prefix} согласована.")
    else:
        print(f"ОС_{prefix} > 0.10 → требуется пересмотр матрицы {prefix}.")

def calculate_S_P(df, w_values, prefix=''):
    """Вычисляет суммы столбцов и P_i"""
    # Суммы столбцов
    print(f"\nВычисление сумм столбцов для {prefix}:")
    S = df.sum()
    for i, s in enumerate(S, start=1):
        elements = ' + '.join(f'{x:.3f}'.rstrip('0').rstrip('.') for x in df[f'A{i}'])
        print(f"S_{prefix}_{i} = {elements} = {s:.3f};")
    
    # P_i = S_i × W_i
    print(f"\nВычисление P_{prefix}i:")
    P = S * w_values
    for i, (s, w, p) in enumerate(zip(S, w_values, P), start=1):
        print(f"P_{prefix}_{i} = S_{prefix}_{i} × W_{prefix}_{i} = {s:.3f} × {w:.3f} = {p:.2f};")
    
    return P

# Основные данные
alternatives = [
    {'name': '1. Сарафаново', 'price': 129, 'weight': 970, 'calories': 46, 'shelf_life': 180},
    {'name': '2. Простоквашино', 'price': 99, 'weight': 930, 'calories': 53, 'shelf_life': 16},
    {'name': '3. Просто', 'price': 85, 'weight': 970, 'calories': 53, 'shelf_life': 180},
    {'name': '4. Искренне ваш', 'price': 85, 'weight': 930, 'calories': 53, 'shelf_life': 16},
    {'name': '5. Зелёная линия', 'price': 79, 'weight': 900, 'calories': 40, 'shelf_life': 10},
]

# Создаем DataFrame с альтернативами
df = pd.DataFrame(alternatives)
df.index = df.index + 1 
print(df, '\n')

# Матрицы сравнений
criteria_data = {
    'К1': [1, 1, 1/3, 1/5],
    'К2': [1, 1, 1/3, 1/5],
    'К3': [3, 3, 1, 1/3],
    'К4': [5, 5, 3, 1]
}
criteria_df = create_dataframe(criteria_data, index=['К1', 'К2', 'К3', 'К4'])
print("Таблица критериев:")
print(criteria_df, '\n')

k1_data = {
    'A1': [1, 1/5, 1/7, 1/7, 1/9],
    'A2': [5, 1, 1/5, 1/5, 1/7],
    'A3': [7, 5, 1, 1, 1/3],
    'A4': [7, 5, 1, 1, 1/3],
    'A5': [9, 7, 3, 3, 1]
}

k2_data = {
    'A1': [1, 5, 1, 5, 7],
    'A2': [1/5, 1, 1/5, 1, 3],
    'A3': [1, 5, 1, 5, 7],
    'A4': [1/5, 1, 1/5, 1, 3],
    'A5': [1/7, 1/3, 1/7, 1/3, 1]
}

k3_data = {
    'A1': [1, 5, 5, 5, 1/3],
    'A2': [1/5, 1, 1, 1, 1/7],
    'A3': [1/5, 1, 1, 1, 1/7],
    'A4': [1/5, 1, 1, 1, 1/7],
    'A5': [3, 7, 7, 7, 1]
}

k4_data = {
    'A1': [1, 9, 1, 9, 9],
    'A2': [1/9, 1, 1/9, 1, 5],
    'A3': [1, 9, 1, 9, 9],
    'A4': [1/9, 1, 1/9, 1, 5],
    'A5': [1/9, 1/5, 1/9, 1/5, 1]
}

# Создаем DataFrame для каждой матрицы сравнений
k1_df = create_dataframe(k1_data, orient='index', columns=['A1', 'A2', 'A3', 'A4', 'A5'])
k2_df = create_dataframe(k2_data, orient='index', columns=['A1', 'A2', 'A3', 'A4', 'A5'])
k3_df = create_dataframe(k3_data, orient='index', columns=['A1', 'A2', 'A3', 'A4', 'A5'])
k4_df = create_dataframe(k4_data, orient='index', columns=['A1', 'A2', 'A3', 'A4', 'A5'])

# Вычисляем веса для каждой матрицы
w2_values, _, _ = calculate_weights(criteria_df, '2')
w_k1_values, _, _ = calculate_weights(k1_df, 'K1')
w_k2_values, _, _ = calculate_weights(k2_df, 'K2')
w_k3_values, _, _ = calculate_weights(k3_df, 'K3')
w_k4_values, _, _ = calculate_weights(k4_df, 'K4')

# Вычисляем согласованность для критериев
P_criteria = calculate_S_P(criteria_df, w2_values, '2')
calculate_consistency(P_criteria, n=4, SI=0.90, prefix='2')

# Вычисляем согласованность для каждой матрицы альтернатив
P_k1 = calculate_S_P(k1_df, w_k1_values, 'K1')
calculate_consistency(P_k1, n=5, SI=1.12, prefix='K1')

P_k2 = calculate_S_P(k2_df, w_k2_values, 'K2')
calculate_consistency(P_k2, n=5, SI=1.12, prefix='K2')

P_k3 = calculate_S_P(k3_df, w_k3_values, 'K3')
calculate_consistency(P_k3, n=5, SI=1.12, prefix='K3')

P_k4 = calculate_S_P(k4_df, w_k4_values, 'K4')
calculate_consistency(P_k4, n=5, SI=1.12, prefix='K4')

# Итоговые веса
print("\nИтоговые значения W:")
print(f"W2i = ({'; '.join(f'{w:.3f}' for w in w2_values)});")
print(f"W3K1Y = ({'; '.join(f'{w:.3f}' for w in w_k1_values)});")
print(f"W3K2Y = ({'; '.join(f'{w:.3f}' for w in w_k2_values)});")
print(f"W3K3Y = ({'; '.join(f'{w:.3f}' for w in w_k3_values)});")
print(f"W3K4Y = ({'; '.join(f'{w:.3f}' for w in w_k4_values)});")

# Рассчет итоговых весов альтернатив
print("\nРассчет итоговых весов альтернатив:")
final_weights = []
for i in range(5):
    w = (w2_values[0] * w_k1_values[i] + 
         w2_values[1] * w_k2_values[i] + 
         w2_values[2] * w_k3_values[i] + 
         w2_values[3] * w_k4_values[i])
    final_weights.append(w)
    print(f"W_{i+1} = {w:.4f}")

# Вывод ранжирования альтернатив
ranking = sorted(zip(df['name'], final_weights), key=lambda x: -x[1])
print("\nРанжирование альтернатив:")
for i, (name, weight) in enumerate(ranking, start=1):
    print(f"{i}. {name}: {weight:.4f}")