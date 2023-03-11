import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

world = []

dx = [1,0,-1,0]
dy = [0,1,0,-1]

for _ in range(n):
    world.append(input().rstrip())
visit_world = [[0 for _ in range(m)] for _ in range(n)]
visit_world_broke_wall = [[0 for _ in range(m)] for _ in range(n)]

pos = (0,0)
length = 1
broke_wall = False
deq = deque()
deq.append((pos,length,broke_wall))
visit_world[0][0] = 1
res = 1e9

while deq:
    p, l, b = deq.popleft()
    y, x = p
    if y == n-1 and x == m-1:
        res = min(res,l)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if b:
                if world[ny][nx] == '0' and visit_world_broke_wall[ny][nx] == 0:
                    visit_world_broke_wall[ny][nx] = 1
                    deq.append(((ny,nx),l+1,b))
            else:
                if world[ny][nx] == '0' and visit_world[ny][nx] == 0:
                    visit_world[ny][nx] = 1
                    deq.append(((ny,nx),l+1,b))
                elif world[ny][nx] == '1':
                    visit_world_broke_wall[ny][nx] = 1
                    deq.append(((ny,nx),l+1,True))
                    
if res == 1e9:
    print("-1")
else:
    print(res)