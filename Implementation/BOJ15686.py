from itertools import combinations
n, m = list(map(int, input().split()))
city = [list(map(int, input().split())) for _ in range(n)]
chicken = []
house = []
min_chicken_load = 0
f = 0
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))
chose_chicken = list(combinations(range(len(chicken)), m))
for i in chose_chicken:
    sum_load = 0
    for y, x in house:
        min_load = abs(chicken[i[0]][0] - y) + abs(chicken[i[0]][1] - x)
        for j in range(1, m):
            tmp = abs(chicken[i[j]][0] - y) + abs(chicken[i[j]][1] - x)
            if tmp < min_load:
                min_load = tmp
        sum_load += min_load
    if f == 0:
        f += 1
        min_chicken_load = sum_load
    else:
        if sum_load < min_chicken_load:
            min_chicken_load = sum_load


print(min_chicken_load)