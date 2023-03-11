import sys
from collections import deque
n, m = map(int, input().split())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

world = [list(map(int, input().split())) for _ in range(n)]
check = [[0] * m for _ in range(n)]

def isDivided(check):
    num = 0
    for i in range(n):
        for j in range(m):
            if check[i][j] != 0 and num == 0:
                bfs(i, j, check)
                num += 1
            elif check[i][j] != 0 and num != 0:
                return True
    return False
                
def bfs(i, j, check):
    deq = deque()
    deq.append((i, j))
    check[i][j] = 0
    while deq:
        y, x = deq.popleft()
        for k in range(4):
            ny, nx = y + dy[k], x + dx[k]
            if 0 <= ny < n and 0 <= nx < m:
                if check[ny][nx] != 0:
                    deq.append((ny, nx))
                    check[ny][nx] = 0
                    
def down():
    tmp = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if world[i][j] != 0:
                cnt = 0
                for k in range(4):
                    ny, nx = i + dy[k], j + dx[k]
                    if 0 <= ny < n and 0 <= nx < m:
                        if world[ny][nx] == 0:
                            cnt += 1
                tmp[i][j] = cnt
    for i in range(n):
        for j in range(m):
            world[i][j] = max(world[i][j] - tmp[i][j], 0)
            if world[i][j] > 0:
                check[i][j] = 1

time = 0
nothing = True
while True:
    down()
    time += 1
    
    nothing = True
    for i in range(n):
        for j in range(m):
            if world[i][j] != 0:
                nothing = False
    if nothing:
        break 
    
    if isDivided(check):
        break
    
    
if nothing:
    print(0)
else:
    print(time)