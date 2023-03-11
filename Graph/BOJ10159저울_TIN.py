import sys
from collections import deque
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
m = int(input())

compare = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    heavy, light = map(int, input().split())
    compare[heavy][light] = 1
    compare[light][heavy] = -1
    
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if compare[i][j] == 0:
                if compare[i][k] != 0 and compare[i][k] == compare[k][j]:
                    compare[i][j] = compare[i][k]
            if i == j:
                compare[i][j] = 2
for i in range(1, n+1):
    cnt = 0
    for j in range(1, n+1):
        if compare[i][j] == 0:
            cnt += 1
    print(cnt)