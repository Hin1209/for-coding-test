import sys
from collections import deque

input = sys.stdin.readline

dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]


def cant_find(size):
    dont_eat = True
    if size > 6:
        size = 7
    for i in range(1, size):
        if fish[i] != 0:
            dont_eat = False
    return dont_eat


def bfs(y, x, size):
    visited = [[False] * len(space) for _ in range(len(space))]
    visited[y][x] = True
    time = 0
    if cant_find(size):
        return False
    d = deque()
    d.append((y, x, time))
    can_eat = []
    while d:
        yy, xx, t = d.popleft()

        for i in range(4):
            ny = yy + dy[i]
            nx = xx + dx[i]
            if 0 <= ny < len(space) and 0 <= nx < len(space):
                if 0 < space[ny][nx] < size and not visited[ny][nx]:
                    t += 1
                    can_eat.append((t, ny, nx))
                    d.append((ny, nx, t + 1))
                    visited[ny][nx] = True
                elif (space[ny][nx] == size or space[ny][nx] == 0) and not visited[ny][nx]:
                    d.append((ny, nx, t + 1))
                    visited[ny][nx] = True
    if can_eat:
        can_eat.sort()
        fish[space[can_eat[0][1]][can_eat[0][2]]] -= 1
        space[can_eat[0][1]][can_eat[0][2]] = 0
        return can_eat[0]
    else:
        return False




N = int(input())

space = [list(map(int, input().split())) for _ in range(N)]

fish = [0, 0, 0, 0, 0, 0, 0]

for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            y = i
            x = j
            space[i][j] = 0
        elif space[i][j] == 1:
            fish[1] += 1
        elif space[i][j] == 2:
            fish[2] += 1
        elif space[i][j] == 3:
            fish[3] += 1
        elif space[i][j] == 4:
            fish[4] += 1
        elif space[i][j] == 5:
            fish[5] += 1
        elif space[i][j] == 6:
            fish[6] += 1

time = 0
shark_size = 2
eat_fish = 0

while True:
    result = bfs(y, x, shark_size)
    if not result:
        print(time)
        break
    eat_fish += 1
    if eat_fish == shark_size:
        eat_fish = 0
        shark_size += 1
    t, y, x = result
    time += t

