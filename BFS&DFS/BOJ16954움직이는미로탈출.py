import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 1, 0, -1, 1, 1, -1, -1, 0]
dy = [1, 0, -1, 0, 1, -1, 1, -1, 0]

world = [[input().rstrip() for _ in range(8)]]
visited = [[[0] * 8 for _ in range(8)] for _ in range(18)]

for i in range(1,10):
    tmp = []
    if i > 8:
        for _ in range(8):
            tmp.append("........")
        world.append(tmp)
        continue
    for _ in range(i):
        tmp.append("........")
    for j in range(8-i):
        tmp.append(world[i-1][j+i-1])
    world.append(tmp)

deq = deque()
deq.append((7, 0, 0))

possible = False
while deq:
    y, x, time = deq.popleft()
    if time > 8:
        possible = True
        break
    if world[time][y][x] == "#": continue
    if y == 0 and x == 7:
        possible = True
        break
    for i in range(9):
        ny, nx = y+dy[i], x+dx[i]
        next_time = time+1
        if 0 <= ny < 8 and 0 <= nx < 8:
            if world[time][ny][nx] == "#": continue
            elif visited[next_time][ny][nx]: continue
            else:
                visited[next_time][ny][nx] = 1
                deq.append((ny, nx, next_time))

print(1) if possible else print(0)
    