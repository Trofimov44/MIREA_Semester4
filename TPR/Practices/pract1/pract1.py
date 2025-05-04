import pandas as pd


alternatives = [
    {'name': '1. Простоквашино', 'price': 99, 'weight': 930, 'calories': 53, 'shelf_life': 16},
    {'name': '2. Домик в деревне', 'price': 89, 'weight': 930, 'calories': 53, 'shelf_life': 15},
    {'name': '3. Молочный знак', 'price': 71, 'weight': 900, 'calories': 53, 'shelf_life': 14},
    {'name': '4. Эко Нива', 'price': 114, 'weight': 1000, 'calories': 60, 'shelf_life': 365},
    {'name': '5. Просто', 'price': 85, 'weight': 970, 'calories': 53, 'shelf_life': 180},
    {'name': '6. Сарафаново', 'price': 129, 'weight': 970, 'calories': 46, 'shelf_life': 180},
    {'name': '7. Зелёная линия', 'price': 79, 'weight': 900, 'calories': 40, 'shelf_life': 10},
    {'name': '8. Искренне ваш', 'price': 85, 'weight': 930, 'calories': 53, 'shelf_life': 16},
    {'name': '9. Экомилк', 'price': 89, 'weight': 900, 'calories': 70, 'shelf_life': 21},
]

df = pd.DataFrame(alternatives)
df.index = df.index + 1
print(df, '\n')

def dominates(a, b):
    # Проверяем, что 'a' не хуже 'b' по всем критериям
    better_in_any = False
    
    if a['price'] > b['price']:  # цена: меньше лучше
        return False
    if a['price'] < b['price']:
        better_in_any = True
        
    if a['weight'] < b['weight']:  # вес: больше лучше
        return False
    if a['weight'] > b['weight']:
        better_in_any = True
        
    if a['calories'] > b['calories']:  # калории: меньше лучше
        return False
    if a['calories'] < b['calories']:
        better_in_any = True
        
    if a['shelf_life'] < b['shelf_life']:  # срок: больше лучше
        return False
    if a['shelf_life'] > b['shelf_life']:
        better_in_any = True
        
    return better_in_any

def compare_alternatives(alternatives):
    relations = {}
    for i, a in enumerate(alternatives):
        relations[a['name']] = {'dominates': [], 'dominated_by': [], 'incomparable': []}
        for j, b in enumerate(alternatives):
            if i == j:
                continue
            if dominates(a, b):
                relations[a['name']]['dominates'].append(b['name'])
            elif dominates(b, a):
                relations[a['name']]['dominated_by'].append(b['name'])
            else:
                relations[a['name']]['incomparable'].append(b['name'])
    return relations

def Lower_boundaries(a):
    if a['weight'] < 950:
        return False
    elif a['shelf_life'] < 20:
        return False
    else:
        return True

def ParetoLowerBoundaries():
    global Lower_bound
    Lower_bound = []
    for i in alternatives:
        if Lower_boundaries(i):
            Lower_bound.append(i['name'])

def dada(a, b):
    global dada_list
    dada_list = []
    for i in a:
        if i in b:
            dada_list.append(i)

def Sub_optimization(a):
    if a['weight'] < 950:
        return False
    elif a['calories'] < 53:
        return False
    elif a['shelf_life'] < 20:
        return False
    else:
        return True

def ParetoSubOptimization():
    global Sub_opt
    Sub_opt = []
    for i in alternatives:
        if Sub_optimization(i):
            Sub_opt.append([i['price'], i['name']])

def lexicographic_optimization(alternatives, criteria_order):
    remaining = alternatives
    for criterion, reverse in criteria_order:
        # Сортируем по текущему критерию
        remaining.sort(key=lambda x: x[criterion], reverse=reverse)
        # Выбираем лучшие по текущему критерию
        best_value = remaining[0][criterion]
        remaining = [alt for alt in remaining if alt[criterion] == best_value]
    return remaining[0] if remaining else None

def main():
    # Сравнение альтернатив
    relations = compare_alternatives(alternatives)
    for alt, rel in relations.items():
        print(f" {alt}|", f" Доминирует: {', '.join(rel['dominates']) if rel['dominates'] else 'Нет'}",
              f" Доминируется: {', '.join(rel['dominated_by']) if rel['dominated_by'] else 'Нет'}")
    print()
    
    # Доминирующие альтернативы
    dominant_alternatives = [alt for alt, rel in relations.items() if rel['dominates']]
    print("Доминирующие альтернативы:")
    for i in sorted(dominant_alternatives):
        print(i)
    print()
    
    # Указание верхних/нижних границ критериев
    print('Указание верхних/нижних границ критериев:')
    print('Установим для таблицы нижнюю границу: вес не менее 950 и срок хранения не менее 20')
    print('Удовлетворяют условиям:')
    ParetoLowerBoundaries()
    for i in sorted(Lower_bound):
        print(i)
    print('Из них оптимальными по Парето является:')
    dada(Lower_bound, dominant_alternatives)
    for i in sorted(dada_list):
        print(i)
    
    # Субоптимизация
    print('\nСубоптимизация:')
    print('Пусть в качестве главного критерия выступает критерий цена.')
    print('Вес не менее 950, калорийность не менее 53, срок хранения не менее 20.')
    print('Удовлетворяют условиям:')
    ParetoSubOptimization()
    for i in sorted(Sub_opt):
        print(i[1])
    print('Из них имеет меньшую цену:')
    print(min(Sub_opt)[1])
    
    # Лексикографическая оптимизация (только для доминирующих альтернатив)
    print('\nЛексикографическая оптимизация (только для доминирующих альтернатив):')
    dominant_alt_objects = [alt for alt in alternatives if alt['name'] in dominant_alternatives]
    criteria_order = [('price', False), ('weight', True), ('calories', False), ('shelf_life', True)]
    optimal = lexicographic_optimization(dominant_alt_objects, criteria_order)
    print(f"Оптимальная альтернатива по лексикографической оптимизации: {optimal['name']}", '\n')

if __name__ == '__main__':
    main()