import sys
from collections import deque 
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

dx = [0, 1, 0, -1, 1, 1, -1, -1]
dy = [1, 0, -1, 0, 1, -1, 1, -1]

n, m = map(int, input().split())

world = []

for i in range(n):
    tmp = list(map(int, input().split()))
    world.append(tmp)
    
deq = deque()

for i in range(n):
    for j in range(m):
        if world[i][j] == 1:
            deq.append((i, j))

while deq:
    y, x = deq.popleft()
    for i in range(8):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= nx < m and 0 <= ny < n:
            if world[ny][nx] == 0:
                world[ny][nx] = world[y][x] + 1
                deq.append((ny, nx))

safe = 0
for i in range(n):
    for j in range(m):
        if safe < world[i][j]:
            safe = world[i][j]
print(safe-1)
