import sys
input = sys.stdin.readline

n = int(input())

world = [] 
for i in range(n):
    world.append(list(map(int, input().split())))

INF = 1e9
for i in range(n):
    for j in range(n):
        if world[i][j] == 0:
            world[i][j] = INF
            
all_visited = 0b0
for i in range(n):
    all_visited |= (1 << i)
dp = [[INF] * n for _ in range(all_visited)]

def find_min(now, visited):
    if visited == all_visited:
        return world[now][0]
    
    if dp[visited][now] != INF:
        return dp[visited][now]
    
    for i in range(1,n):
        if world[now][i] != INF:
            if visited & (1 << i):
                continue
            dp[visited][now] = min(dp[visited][now], find_min(i, visited | (1 << i)) + world[now][i])
    return dp[visited][now]
print(find_min(0,1))
