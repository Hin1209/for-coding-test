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
for i in range(len(chicken)):
    for j in range(1, len(chicken)):
        sum_load = 0
        if(i + j * (m-1) >= len(chicken)):
            break
        tmp_chicken = []
        for k in range(m):
            tmp_chicken.append(chicken[i+j*k])
        for z in range(len(house)):
            min_load = abs(tmp_chicken[0][0] - house[z][0]) + abs(tmp_chicken[0][1] - house[z][1])
            for l in range(1, len(tmp_chicken)):
                tmp_load = abs(tmp_chicken[l][0] - house[z][0]) + abs(tmp_chicken[l][1] - house[z][1])
                if tmp_load < min_load:
                    min_load = tmp_load
            sum_load += min_load
        if f == 0:
            min_chicken_load = sum_load
            f += 1
        else:
            if min_chicken_load > sum_load:
                min_chicken_load = sum_load
print(min_chicken_load)