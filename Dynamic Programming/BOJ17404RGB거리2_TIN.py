import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
distance = []

for _ in range(n):
    r, g, b = map(int, input().split())
    distance.append([r, g, b])

INF = 1e9
dp_r = [[INF, INF, INF] for _ in range(n)]
dp_g = [[INF, INF, INF] for _ in range(n)]
dp_b = [[INF, INF, INF] for _ in range(n)]
dp_r[0][0] = distance[0][0]
dp_g[0][1] = distance[0][1]
dp_b[0][2] = distance[0][2]

for i in range(1, n-1):
    dp_r[i][0] = min(dp_r[i-1][1] + distance[i][0], dp_r[i-1][2] + distance[i][0])
    dp_r[i][1] = min(dp_r[i-1][0] + distance[i][1], dp_r[i-1][2] + distance[i][1])
    dp_r[i][2] = min(dp_r[i-1][0] + distance[i][2], dp_r[i-1][1] + distance[i][2])

    dp_g[i][0] = min(dp_g[i-1][1] + distance[i][0], dp_g[i-1][2] + distance[i][0])
    dp_g[i][1] = min(dp_g[i-1][0] + distance[i][1], dp_g[i-1][2] + distance[i][1])
    dp_g[i][2] = min(dp_g[i-1][0] + distance[i][2], dp_g[i-1][1] + distance[i][2])

    dp_b[i][0] = min(dp_b[i-1][1] + distance[i][0], dp_b[i-1][2] + distance[i][0])
    dp_b[i][1] = min(dp_b[i-1][0] + distance[i][1], dp_b[i-1][2] + distance[i][1])
    dp_b[i][2] = min(dp_b[i-1][0] + distance[i][2], dp_b[i-1][1] + distance[i][2])

dp_r[n-1][1] = min(dp_r[n-2][0] + distance[n-1][1], dp_r[n-2][2] + distance[n-1][1])
dp_r[n-1][2] = min(dp_r[n-2][0] + distance[n-1][2], dp_r[n-2][1] + distance[n-1][2])
dp_g[n-1][0] = min(dp_g[n-2][1] + distance[n-1][0], dp_g[n-2][2] + distance[n-1][0])
dp_g[n-1][2] = min(dp_g[n-2][0] + distance[n-1][2], dp_g[n-2][1] + distance[n-1][2])
dp_b[n-1][0] = min(dp_b[n-2][1] + distance[n-1][0], dp_b[n-2][2] + distance[n-1][0])
dp_b[n-1][1] = min(dp_b[n-2][0] + distance[n-1][1], dp_b[n-2][2] + distance[n-1][1])
print(min(dp_r[n-1][1],dp_r[n-1][2],dp_g[n-1][0],dp_g[n-1][2],dp_b[n-1][0],dp_b[n-1][1]))