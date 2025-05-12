# Дан список курсов университета и их пререквизитов. Нужно определить,
# можно ли окончить все курсы, и если да, то вывести один из возможных порядков их изучения.
#
# Формат ввода:
# Первая строка: n (число курсов), m (число зависимостей).
# Следующие m строк: a b (курс b требует прохождения курса a).
#
# Формат вывода:
# Если циклов нет, вывести любой допустимый порядок курсов.
# Если есть цикл, вывести -1.

# Пример 1 (нет циклов)
# Ввод:
# 4 3
# 1 2
# 2 3
# 1 4
# Граф:
# 1 → 2 → 3
# 1 → 4
# Вывод:
# 1 2 4 3  # Или 1 4 2 3

# Пример 2 (есть цикл)
# Ввод:
# 3 3
# 1 2
# 2 3
# 3 1
# Граф:
# 1 → 2 → 3 → 1 (цикл!)
# Вывод:
# -1
def Kann(graf):
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
            if len(queue) == 0:
                return [-1]
            return queue
        i += 1
        lst = graf[vert]
        for el in lst:
            dct[el] -= 1
            if dct[el] == 0:
                if el in queue:
                    return [-1]
                queue.append(el)


n, m = map(int, input().split())
graf = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    a, b = map(int, input().split())
    graf[a].append(b)
print(*Kann(graf))
