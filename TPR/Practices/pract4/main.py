import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# 1. Создаем данные для графиков ограничений
x1 = np.linspace(0, 40, 400)  # Значения x1 от 0 до 40

# Ограничение 1: x1 + 8x2 <= 36
x2_1 = (36 - x1) / 8  # x2 = (36 - x1) / 8
    
# Ограничение 2: 2x1 + 3x2 <= 20
x2_2 = (20 - 2 * x1) / 3  # x2 = (20 - 2x1) / 3

# 2. Находим точки пересечения для ОДР
# Точка пересечения прямых x1 + 8x2 = 36 и 2x1 + 3x2 = 20
# Решаем систему: x1 + 8x2 = 36 и 2x1 + 3x2 = 20
A = np.array([[1, 8], [2, 3]])
B = np.array([36, 20])
intersection = np.linalg.solve(A, B)  # (4, 4)

# Вершины ОДР: (0,0), (0, 4.5), (4, 4), (10, 0)
vertices = [(0, 0), (0, 4.5), (4, 4), (10, 0)]

# 3. Создаем график
plt.figure(figsize=(8, 6))

# Ограничение 1
plt.plot(x1, x2_1, label=r'$x_1 + 8x_2 \leq 36$', color='blue')
plt.fill_between(x1, 0, x2_1, where=(x2_1 >= 0), alpha=0.1, color='blue')

# Ограничение 2
plt.plot(x1, x2_2, label=r'$2x_1 + 3x_2 \leq 20$', color='green')
plt.fill_between(x1, 0, x2_2, where=(x2_2 >= 0), alpha=0.1, color='green')

# 4. ОДР (область пересечения)
poly = Polygon(vertices, closed=True, fill=True, facecolor='orange', edgecolor='black', alpha=0.3, label='ОДР')
plt.gca().add_patch(poly)

# 5. Целевая функция: x1 + 3x2 = c
# Для минимума (c = 0) и максимума (c = 16)
x1_range = np.array([0, 40])
x2_f_min = (0 - x1_range) / 3  # c = 0
x2_f_max = (16 - x1_range) / 3  # c = 16 (максимум в точке (4, 4))



# 6. Точки минимума и максимума
plt.plot(0, 0, 'ro', label='Минимум (0, 0): f(x) = 0')  # Минимум
plt.plot(4, 4, 'mo', label='Максимум (4, 4): f(x) = 16')  # Максимум

# 7. Градиент (1, 3)
plt.arrow(0, 0, 1, 2.9, head_width=0.1, head_length=0.1, fc='k', ec='k', label='Градиент (1, 3)')

# 8. Настройки графика
plt.xlim(-1, 12)
plt.ylim(-1, 7)
plt.xlabel(r'$x_1$')
plt.ylabel(r'$x_2$')
plt.grid(True)
plt.legend()
plt.title('Графический метод: ОДР и экстремумы')

# Показать график
plt.show()

# 9. Вывод результатов
print("Минимум: f(x) = 0 в точке (0, 0)")
print("Максимум: f(x) = 16 в точке (4, 4)")