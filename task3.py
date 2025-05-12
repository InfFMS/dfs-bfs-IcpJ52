# Реализовать алгоритм Кана для топологической сортировки
# Пример с пошаговой работой алгоритма
# Граф: A → B → C
#       A → D

graf = {"A": ["B", "C"],
        "B": ["C"],
        "C": [],
        "D": []}

# Шаги:
# 1. Начальные вершины без входящих рёбер: [A]
# 2. Обрабатываем A → результат [A], обновляем степени B(1→0), D(1→0)
# 3. Вершины для обработки: [B, D]
# 4. Обрабатываем B → результат [A,B], обновляем степень C(1→0)
# 5. Обрабатываем D → результат [A,B,D]
# 6. Обрабатываем C → результат [A,B,D,C]
# 7. Все вершины обработаны → сортировка завершена
dct = {el: 0 for el in graf}
for val in graf.values():
    for el in dct:
        if el in val:
            dct[el] += 1
queue = []
for el in dct:
    if dct[el] == 0:
        queue.append(el)
i = 0
while True:
    try:
        vert = queue[i]
    except IndexError:
        print(queue)
        break
    i += 1
    lst = graf[vert]
    for el in lst:
        dct[el] -= 1
        if dct[el] == 0:
            queue.append(el)
