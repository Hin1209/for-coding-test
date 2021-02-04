import sys
from collections import deque

input = sys.stdin.readline

INF = int(1e9)
N, K = map(int, input().split())
q = deque()
q.append(N)

position = [INF] * (100001)
position[N] = 0
while q:
    m = q.popleft()
    if m < 100000:
        if position[m+1] > position[m] + 1:
            q.append(m+1)
            position[m+1] = position[m] + 1
    if m > 0:
        if position[m - 1] > position[m] + 1:
            q.append(m - 1)
            position[m - 1] = position[m] + 1
    if 2 * m < 100001:
        if position[2 * m] > position[m] + 1:
            q.append(2 * m)
            position[2 * m] = position[m] + 1

print(position[K])