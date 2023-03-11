import sys
from collections import deque

input = sys.stdin.readline
INF = int(1e9)
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

n = int(input())

world = [input().rstrip() for _ in range(n)]
start = 0
end = 0

for i in range(n):
    for j in range(n):
        if world[i][j] == "#":
            if start == 0:
                start = (i, j)
            else:
                end = (i, j)
                
visited = [[[INF] * 4 for _ in range(n)] for _ in range(n)]

deq = deque()
deq.append((start[0], start[1], 0, 0))
deq.append((start[0], start[1], 1, 0))
deq.append((start[0], start[1], 2, 0))
deq.append((start[0], start[1], 3, 0))
res = INF

while deq:
    y, x, direction, cnt = deq.popleft()
    if y == end[0] and x == end[1]: 
        res = min(res, cnt) 
        continue

    ny, nx = y+dy[direction], x+dx[direction]
    if 0 <= ny < n and 0 <= nx < n:
        if world[ny][nx] != "*" and visited[ny][nx][direction] > cnt: 
            visited[ny][nx][direction] = cnt
            deq.append((ny, nx, direction, cnt))

    if world[y][x] == "!":
        for i in range(1, 4):
            next_direction = (direction+i) % 4
            if (next_direction + direction) % 2 == 0: continue
        
            ny, nx = y+dy[next_direction], x+dx[next_direction]
            if 0 <= ny < n and 0 <= nx < n:
                if world[ny][nx] != "*" and visited[ny][nx][next_direction] > cnt+1: 
                    visited[ny][nx][next_direction] = cnt+1
                    deq.append((ny, nx, next_direction, cnt+1))
print(res)