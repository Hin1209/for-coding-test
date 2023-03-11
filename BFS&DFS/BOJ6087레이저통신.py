import sys
from collections import deque

input = sys.stdin.readline
INF = int(1e9)
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

w, h = map(int, input().split())

world = [input().rstrip() for _ in range(h)]
start = 0
end = 0

for i in range(h):
    for j in range(w):
        if world[i][j] == "C":
            if start == 0:
                start = (i, j)
            else:
                end = (i, j)
                
visited = [[INF] * w for _ in range(h)]

deq = deque()
deq.append((start[0], start[1], 0, 0, 0))
deq.append((start[0], start[1], 1, 0, 0))
deq.append((start[0], start[1], 2, 0, 0))
deq.append((start[0], start[1], 3, 0, 0))

while deq:
    y, x, direction, cnt, isPass = deq.popleft()
    if y == end[0] and x == end[1]: continue 

    ny, nx = y+dy[direction], x+dx[direction]
    if 0 <= ny < h and 0 <= nx < w:
        if world[ny][nx] != "*" and visited[ny][nx] >= cnt:
            visited[ny][nx] = cnt
            deq.append((ny, nx, direction, cnt, 0))

    if isPass: continue

    for i in range(1, 4):
        next_direction = (direction+i) % 4
        if (next_direction + direction) % 2 == 0: continue
        
        ny, nx = y+dy[next_direction], x+dx[next_direction]
        if 0 <= ny < h and 0 <= nx < w:
            if world[ny][nx] != "*" and visited[ny][nx] > cnt+1:
                visited[ny][nx] = cnt+1
                deq.append((ny, nx, next_direction, cnt+1, 0))
            elif world[ny][nx] != "*" and visited[ny][nx] == cnt+1:
                deq.append((ny, nx, next_direction, cnt+1, 1))
print(visited[end[0]][end[1]])