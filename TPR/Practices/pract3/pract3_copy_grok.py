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

# Универсальная функция для расчёта весов и согласованности
def calculate_weights_and_consistency(df, n, SI, label, indices):
    # Вычисление весов W
    row_products = df.prod(axis=1)
    row_roots = row_products ** (1 / n)
    sum_v = row_roots.sum()
    W = row_roots / sum_v
    
    # Вывод промежуточных результатов
    print(f"\n--- {label} ---")
    print("Вычисление V:")
    for i, v in enumerate(row_roots, 1):
        print(f"V_{indices}{i} = ({'x'.join(map(str, df.iloc[i-1]))})^(1/{n}) = {v:.3f}")
    print(f"ΣV = {' + '.join(f'{v:.3f}' for v in row_roots)} = {sum_v:.3f}")
    print("Вычисление W:")
    w_values = [f"{w:.3f}" for w in W]
    for i, (v, w) in enumerate(zip(row_roots, W), 1):
        print(f"W_{indices}{i} = {v:.3f} / {sum_v:.3f} = {w:.3f}")
    print(f"W_{indices}i = ({'; '.join(w_values)})")
    
    # Проверка согласованности
    S = df.sum()
    P = S * W
    lambda_max = P.sum()
    IC = (lambda_max - n) / (n - 1) if n > 1 else 0
    OC = IC / SI if SI != 0 else 0
    
    # Вывод согласованности
    print(f"\nλ_max = {lambda_max:.2f}")
    print(f"ИС = (λ_max - n)/(n - 1) = ({lambda_max:.2f} - {n})/({n-1}) = {IC:.4f}")
    print(f"ОС = ИС/СИ = {IC:.4f}/{SI} = {OC:.3f}")
    print("Матрица согласована." if OC <= 0.10 else "Требуется пересмотр матрицы.")
    
    return W

# Данные таблиц
criteria_data = {'К1': [1, 1, 1/3, 1/5], 'К2': [1, 1, 1/3, 1/5], 'К3': [3, 3, 1, 1/3], 'К4': [5, 5, 3, 1]}
criteria_df = pd.DataFrame(criteria_data, index=['К1', 'К2', 'К3', 'К4'], dtype=float)
print("Таблица критериев:\n", criteria_df, '\n')

k1_data = {'A1': [1, 1/5, 1/7, 1/7, 1/9], 'A2': [5, 1, 1/5, 1/5, 1/7], 'A3': [7, 5, 1, 1, 1/3], 'A4': [7, 5, 1, 1, 1/3], 'A5': [9, 7, 3, 3, 1]}
k1_df = pd.DataFrame(k1_data, index=['A1', 'A2', 'A3', 'A4', 'A5'], dtype=float)
print("Таблица K1:\n", k1_df, '\n')

k2_data = {'A1': [1, 5, 1, 5, 7], 'A2': [1/5, 1, 1/5, 1, 3], 'A3': [1, 5, 1, 5, 7], 'A4': [1/5, 1, 1/5, 1, 3], 'A5': [1/7, 1/3, 1/7, 1/3, 1]}
k2_df = pd.DataFrame(k2_data, index=['A1', 'A2', 'A3', 'A4', 'A5'], dtype=float)
print("Таблица K2:\n", k2_df, '\n')

k3_data = {'A1': [1, 5, 5, 5, 1/3], 'A2': [1/5, 1, 1, 1, 1/7], 'A3': [1/5, 1, 1, 1, 1/7], 'A4': [1/5, 1, 1, 1, 1/7], 'A5': [3, 7, 7, 7, 1]}
k3_df = pd.DataFrame(k3_data, index=['A1', 'A2', 'A3', 'A4', 'A5'], dtype=float)
print("Таблица K3:\n", k3_df, '\n')

k4_data = {'A1': [1, 9, 1, 9, 9], 'A2': [1/9, 1, 1/9, 1, 5], 'A3': [1, 9, 1, 9, 9], 'A4': [1/9, 1, 1/9, 1, 5], 'A5': [1/9, 1/5, 1/9, 1/5, 1]}
k4_df = pd.DataFrame(k4_data, index=['A1', 'A2', 'A3', 'A4', 'A5'], dtype=float)
print("Таблица K4:\n", k4_df, '\n')

# Расчёты
W2i = calculate_weights_and_consistency(criteria_df, 4, 0.90, "Критерии", "")
W3K1Y = calculate_weights_and_consistency(k1_df, 5, 1.12, "K1", "K1")
W3K2Y = calculate_weights_and_consistency(k2_df, 5, 1.12, "K2", "K2")
W3K3Y = calculate_weights_and_consistency(k3_df, 5, 1.12, "K3", "K3")
W3K4Y = calculate_weights_and_consistency(k4_df, 5, 1.12, "K4", "K4")

# Итоговые веса W1-W5 с исправлением предупреждений
W = [sum(W2i.iloc[j] * W3K[j] for j in range(4)) for W3K in zip(W3K1Y, W3K2Y, W3K3Y, W3K4Y)]
print("\nИтоговые веса для альтернатив:")
for i, w in enumerate(W, 1):
    terms = [f"{W2i.iloc[j]:.3f} × {w3k:.3f}" for j, w3k in enumerate([W3K1Y.iloc[i-1], W3K2Y.iloc[i-1], W3K3Y.iloc[i-1], W3K4Y.iloc[i-1]])]
    print(f"W{i} = {' + '.join(terms)} = {w:.3f}")

# Вывод ранжирования альтернатив
print("\nРанжирование альтернатив:")
alt_names = [alt['name'] for alt in alternatives]
for name, weight in sorted(zip(alt_names, W), key=lambda x: x[1], reverse=True):
    print(f"{name}: {weight:.3f}")