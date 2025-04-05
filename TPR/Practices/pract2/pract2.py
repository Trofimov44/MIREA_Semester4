import pandas as pd
import numpy as np


alternatives = [
    {'name': '1. Простоквашино', 'price': 10, 'weight': 10, 'calories': 10, 'shelf_life': 10},
    {'name': '2. Домик в деревне', 'price': 5, 'weight': 10, 'calories': 10, 'shelf_life': 10},
    {'name': '3. Молочный знак', 'price': 5, 'weight': 10, 'calories': 10, 'shelf_life': 5},
    {'name': '4. Эко Нива', 'price': 15, 'weight': 15, 'calories': 15, 'shelf_life': 15},
    {'name': '5. Просто', 'price': 10, 'weight': 10, 'calories': 10, 'shelf_life': 15},
    {'name': '6. Сарафаново', 'price': 15, 'weight': 10, 'calories': 5, 'shelf_life': 15},
    {'name': '7. Зелёная линия', 'price': 5, 'weight': 5, 'calories': 5, 'shelf_life': 10},
    {'name': '8. Искренне ваш', 'price': 10, 'weight': 10, 'calories': 10, 'shelf_life': 10},
    {'name': '9. Экомилк', 'price': 10, 'weight': 5, 'calories': 15, 'shelf_life': 15},
]

df = pd.DataFrame(alternatives)
df.index = df.index + 1
print(df, '\n')

arr_sign = (5, 5, 4, 3)
C = 1.8

arr = np.zeros((9,9), dtype=object)

for i in range(len(alternatives)):
    for j in range(i + 1, len(alternatives)):
        P = 0
        N = 0

        Dij = ''
        Dji = ''
        print(f"Рассмотрим альтернативы {i+1} и {j+1} (i = {i+1}, j = {j+1}):")
        if alternatives[i]['price'] == alternatives[j]['price']:
            Dij += '0 + '
            Dji += '0 + '
            pass
        elif alternatives[i]['price'] < alternatives[j]['price']:
            P += arr_sign[0]
            Dij += f'{arr_sign[0]} + '
            Dji += '0 + '
        else:
            N += arr_sign[0]
            Dij += '0 + '
            Dji += f'{arr_sign[0]} + '

        if alternatives[i]['weight'] == alternatives[j]['weight']:
            Dij += '0 + '
            Dji += '0 + '
            pass
        elif alternatives[i]['weight'] > alternatives[j]['weight']:
            P += arr_sign[1]
            Dij += f'{arr_sign[1]} + '
            Dji += '0 + '
        else:
            N += arr_sign[1]
            Dij += '0 + '
            Dji += f'{arr_sign[1]} + '

        if alternatives[i]['calories'] == alternatives[j]['calories']:
            Dij += '0 + '
            Dji += '0 + '
            pass
        elif alternatives[i]['calories'] < alternatives[j]['calories']:
            P += arr_sign[2]
            Dij += f'{arr_sign[2]} + '
            Dji += '0 + '
        else:
            N += arr_sign[2]
            Dij += '0 + '
            Dji += f'{arr_sign[2]} + '

        if alternatives[i]['shelf_life'] == alternatives[j]['shelf_life']:
            Dij += '0'
            Dji += '0'
            pass
        elif alternatives[i]['shelf_life'] > alternatives[j]['shelf_life']:
            P += arr_sign[3]
            Dij += f'{arr_sign[3]}'
            Dji += '0'
        else:
            N += arr_sign[3]
            Dij += '0'
            Dji += f'{arr_sign[3]}'


        D = 0
        if N == P:
            print(f"D{i+1}{j+1} P и N равны")
            pass

        print(f"P{i + 1}{j + 1} = {Dij} = {P}")
        print(f"N{i + 1}{j + 1} = {Dji} = {N}")
        if N == 0:
            print(f"D{i+1}{j+1} = P{i+1}{j+1}/N{i+1}{j+1}  = {P}/{N} - Деление на ноль, отбрасываем")
        elif P == 0:
            print(f"D{i+1}{j+1} = P{i+1}{j+1}/N{i+1}{j+1} = {P}/{N} = {round(P/N, 1)} - inf - принимаем")
            arr[i, j] = np.inf
        elif P/N < 1:
            print(f"D{i+1}{j+1} = P{i+1}{j+1}/N{i+1}{j+1} = {P}/{N} = {round(P/N, 1)} < 1 - отбрасываем")
        elif P/N > 1:
            print(f"D{i+1}{j+1} = P{i+1}{j+1}/N{i+1}{j+1} = {P}/{N} = {round(P/N, 1)} > 1 - принимаем")
            arr[i,j] = round(P/N, 1)

        print(f"P{j + 1}{i + 1} = {Dji} = {N}")
        print(f"N{j + 1}{i + 1} = {Dij} = {P}")
        if P == 0:
            print(f"D{j+1}{i+1} = N{j+1}{i+1}/P{j+1}{i+1} = {N}/{P} - Деление на ноль, отбрасываем")
        elif N == 0:
            print(f"D{j+1}{i+1} = N{j+1}{i+1}/P{j+1}{i+1} = {N}/{P} - inf - принимаем")
            arr[j, i] = np.inf
        elif N/P < 1:
            print(f"D{j+1}{i+1} = N{j+1}{i+1}/P{j+1}{i+1} = {N}/{P} = {round(N/P, 1)} < 1 - отбрасываем")
        elif N/P > 1:
            print(f"D{j+1}{i+1} = N{j+1}{i+1}/{j+1}{i+1} = {N}/{P} = {round(N/P, 1)} > 1 - принимаем")
            arr[j, i] = round(N / P, 1)
        print()

print('Полная матрица предпочтений альтернатив.')
for i in range(9):
    arr[i,i] = 'X'
df1 = pd.DataFrame(arr)
df1.index += 1
df1.columns += 1
print(df1, '\n')

print(f"Матрица предпочтений проектов, при пороге С = {C}")
arr[arr == 'X'] = 42
arr[arr < C] = 0
arr[arr == 42] = 'X'

df1 = pd.DataFrame(arr)
df1.index += 1
df1.columns += 1
print(df1)

# Подсчет количества связей для каждой альтернативы
connections = {}

for i in range(len(arr)):
    horizontal = sum(1 for x in arr[i] if x != 0 and x != 'X')
    vertical = sum(1 for x in arr[:, i] if x != 0 and x != 'X')
    connections[i + 1] = (horizontal, vertical)

# Сортировка по количеству связей по горизонтали
sorted_connections = sorted(connections.items(), key=lambda x: x[1][0], reverse=True)


print("\nОтсортированные альтернативы:")
for alt, (h, v) in sorted_connections:
    print(f"{alt}:({h}, {v})")