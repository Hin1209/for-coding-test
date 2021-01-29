from itertools import combinations
n, m = list(map(int, input().split()))
city = [list(map(int, input().split())) for _ in range(n)]
chicken = [] # 치킨집의 위치를 저장
house = [] # 집의 위치를 저장
min_chicken_load = 0 # 가장 짧은 치킨 거리
f = 0 # 반복문을 처음 돌릴때를 대비해 만든 변수
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append((i, j)) # 집 위치 저장
        elif city[i][j] == 2:
            chicken.append((i, j)) # 치킨집 위치 저장
chose_chicken = list(combinations(range(len(chicken)), m)) # m개의 치킨집을 고르는 경우를 모두 저장함
for i in chose_chicken: # i에 골라진 m개의 인덱스가 저장
    sum_load = 0 # 고른 경우에 대한 최소 치킨 거리를 구함
    for y, x in house: # 한 집에서 가장 가까운 치킨집과의 거리를 구함
        min_load = abs(chicken[i[0]][0] - y) + abs(chicken[i[0]][1] - x)
        for j in range(1, m):
            tmp = abs(chicken[i[j]][0] - y) + abs(chicken[i[j]][1] - x)
            if tmp < min_load:
                min_load = tmp
        sum_load += min_load
    if f == 0: # 반복문이 처음이면
        f += 1
        min_chicken_load = sum_load # 최소 치킨 거리를 처음 나온 값으로 저장해둠
    else:
        if sum_load < min_chicken_load:
            min_chicken_load = sum_load


print(min_chicken_load)