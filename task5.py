# Напишите алгоритм поиска в ширину (BFS)
#
# Формат входных данных:
# Граф задаётся в виде словаря, где ключи — вершины, а значения — списки смежных вершин.
#
# Обход начинается с заданной стартовой вершины.
# Требуется:
# 1.Реализовать BFS — обход графа в ширину.
# 2.Вернуть самый коротки маршрут от точки старта до точки назначения.
# Пример входных данных
# city_map = {  
#     'Home': ['Park', 'School', 'Mail'],  
#     'Park': ['Home', 'Museum', 'Cafe'],  
#     'School': ['Home', 'Library', 'Mail'],  
#     'Mail': ['Home', 'School', 'Hospital'],  
#     'Library': ['School', 'Hospital'],  
#     'Hospital': ['Library', 'Mail', 'Office'],  
#     'Cafe': ['Park', 'Theater', 'Office'],  
#     'Museum': ['Park', 'Shop'],  
#     'Shop': ['Museum', 'Theater'],  
#     'Theater': ['Shop', 'Cafe'],  
#     'Office': ['Cafe', 'Hospital']  
# }
# start = "Home"
# finish = "Theater"
#
# Пример выходных данных
# ['Home', 'Park', 'Cafe', 'Theater']
from collections import deque

city_map = {
    'Home': ['Park', 'School', 'Mail'],
    'Park': ['Home', 'Museum', 'Cafe'],
    'School': ['Home', 'Library', 'Mail'],
    'Mail': ['Home', 'School', 'Hospital'],
    'Library': ['School', 'Hospital'],
    'Hospital': ['Library', 'Mail', 'Office'],
    'Cafe': ['Park', 'Theater', 'Office'],
    'Museum': ['Park', 'Shop'],
    'Shop': ['Museum', 'Theater'],
    'Theater': ['Shop', 'Cafe'],
    'Office': ['Cafe', 'Hospital']
}
start = "Home"
finish = "Theater"
dct = {start: [start]}
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
        else:
            tmp = dct[cur] + [el]
            if len(tmp) < len(dct[el]):
                dct[el] = tmp
                for key in dct:
                    val = dct[key]
                    if el in val:
                        dct[key] = tmp + val[val.index(el) + 1:]
    if cur not in visited:
        visited.append(cur)
print(dct)
