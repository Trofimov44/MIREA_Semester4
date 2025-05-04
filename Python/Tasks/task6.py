def compute_Oo(K):
    """Вычисляет множество Oo на основе K."""
    return {abs(k) - 3 * k for k in K if not (-42 < k < 76)}


def compute_Phi(Oo):
    """Вычисляет множество Phi на основе Oo."""
    return {o for o in Oo if o >= 90 or o <= -66}


def compute_sum_squares(N):
    """Вычисляет сумму квадратов элементов множества N."""
    return sum(v * v for v in N)


def compute_sum_products(N, Phi):
    """Вычисляет сумму произведений v * phi для всех пар (v, phi) из N × Phi."""
    return sum(v * phi for v in N for phi in Phi)


def main(K):
    """Вычисляет целочисленную функцию ξ на основе входного множества K."""
    # Шаг 1: Определяем множество Oo
    Oo = compute_Oo(K)

    # Шаг 2: Определяем множество Phi
    Phi = compute_Phi(Oo)

    # Шаг 3: Определяем множество N
    N = K.union(Oo)

    # Шаг 4: Вычисляем ξ
    sum_squares = compute_sum_squares(N)
    sum_products = compute_sum_products(N, Phi)
    xi = sum_squares - sum_products

    return xi

# Тестовые примеры
K1 = {1, 35, -24, -54, 77, 48, 88, 24, 90, 29}
K2 = {-60, -90, 39, -87, -18, -50, -79, 53, -10, -8}

# Вычисляем и выводим результаты
print(f"ξ для K1 = {main(K1)}")  # Ожидаемый результат: 1698490
print(f"ξ для K2 = {main(K2)}")  # Ожидаемый результат: -1208468