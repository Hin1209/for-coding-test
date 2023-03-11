import sys
sys.setrecursionlimit(10**7)

n, m, r = map(int, input().split())
temp = list(map(int, input().split()))
items = [0] * (len(temp) + 1)
for i in range(n):
    items[i+1] = temp[i]
INF = 1e9 
world = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(r):
    start, end, cost = map(int, input().split())
    world[start][end] = cost
    world[end][start] = cost
    
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i == j:
                world[i][j] = 0
            world[i][j] = min(world[i][j], world[i][k] + world[k][j])

get_items = 0 
for i in range(1,n+1):
    tmp_items = 0
    for j in range(1,n+1):
        if world[i][j] <= m:
            tmp_items += items[j]
    get_items = max(get_items, tmp_items)
print(get_items)