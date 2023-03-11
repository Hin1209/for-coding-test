import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
size = []
for i in range(n):
    r, c = map(int, input().split())
    size.append((r, c))

def calculate_cnt(r1, c1, c2):
    return r1 * c1 * c2
INF = 1e9
dp = [[0] * n for _ in range(n)]
for i in range(n):
    dp[i][i] = 0
if n == 1:
    print(0)
else:
    for i in range(1,n):
        for j in range(n-i):
            if i+j != j:
                dp[j][i+j] = INF
            for k in range(j, i+j):
                dp[j][i+j] = min(dp[j][i+j], dp[j][k] + dp[k+1][j+i] + calculate_cnt(size[j][0], size[k][1], size[j+i][1]))
    print(dp[0][n-1])
