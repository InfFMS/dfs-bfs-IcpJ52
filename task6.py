# Дан взвешенный граф.
# Необходимо ответить на следующие вопросы:
# 
# 1. Найти длину всех наикратчайших маршрутов из 'Home' в любую точку на графе? (Просто применить алгоритм Дейкстры)
# 2. Найти как выглядит самый кротчайший маршрут из 'Home' в 'Theater' (вывести последовательность прохождения вершин)?
# Подсказка:
# Удобно хранить значения о пройденном маршруте в виде словаря, где ключ - это текущая вершина, а значение - вершина, из которой мы попали в текущую
# Потом в конце нужно будет просто пройтись по такому словарю от финиша к старту и развернуть его.
#
# Входные данные:
# city_map = {
#     'Home': {'Park': 2, 'School': 5, 'Mail': 10},
#     'Park': {'Home': 2, 'Museum': 4, 'Cafe': 3},
#     'School': {'Home': 5, 'Library': 6, 'Mail': 2},
#     'Mail': {'Home': 10, 'School': 2, 'Hospital': 3},
#     'Library': {'School': 6, 'Hospital': 1},
#     'Hospital': {'Library': 1, 'Mail': 3, 'Office': 4},
#     'Cafe': {'Park': 3, 'Theater': 8, 'Office': 7},
#     'Museum': {'Park': 4, 'Shop': 5},
#     'Shop': {'Museum': 5, 'Theater': 1},
#     'Theater': {'Shop': 1, 'Cafe': 8},
#     'Office': {'Cafe': 7, 'Hospital': 4}
# }
from collections import deque
from math import inf

city_map = {
    'Home': {'Park': 2, 'School': 5, 'Mail': 10},
    'Park': {'Home': 2, 'Museum': 4, 'Cafe': 3},
    'School': {'Home': 5, 'Library': 6, 'Mail': 2},
    'Mail': {'Home': 10, 'School': 2, 'Hospital': 3},
    'Library': {'School': 6, 'Hospital': 1},
    'Hospital': {'Library': 1, 'Mail': 3, 'Office': 4},
    'Cafe': {'Park': 3, 'Theater': 8, 'Office': 7},
    'Museum': {'Park': 4, 'Shop': 5},
    'Shop': {'Museum': 5, 'Theater': 1},
    'Theater': {'Shop': 1, 'Cafe': 8},
    'Office': {'Cafe': 7, 'Hospital': 4}
}
start = "Home"
finish = "Theater"
dct = {start: [start]}
dct1 = {start: 0}
for el in city_map:
    if el != start:
        dct1[el] = inf
visited = []
queue = deque()
queue.append(start)
while True:
    try:
        cur = queue.popleft()
    except IndexError:
        print(visited)
        break
    for el in city_map[cur]:
        if el not in visited:
            queue.append(el)
        if el not in dct:
            dct[el] = dct[cur] + [el]
            dct1[el] = dct1[cur] + city_map[cur][el]
        else:
            tmp = dct[cur] + [el]
            tmp1 = dct1[cur] + city_map[cur][el]
            if dct1[el] > tmp1:
                dct[el] = tmp
                for key in dct:
                    val = dct[key]
                    if el in val:
                        dct[key] = tmp + val[val.index(el) + 1:]
                        dct1[key] = tmp1
    if cur not in visited:
        visited.append(cur)
print(dct1)
print(dct[finish])
