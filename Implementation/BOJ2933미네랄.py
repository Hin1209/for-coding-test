import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

R, C = map(int, input().split())
tmp = [input().rstrip() for _ in range(R)]
N = int(input())
sticks = list(map(int, input().split()))

cave = [[0] * C for _ in range(R)]

for i in range(R):
    for j in range(C):
        if tmp[i][j] == 'x':
            cave[i][j] = 1

def check_drop(y, x, cluster, visited):
    deq = deque()
    deq.append((y, x))
    visited[y][x] = cluster 
    is_drop = True
    while deq:
        y, x = deq.popleft()
        if y == R-1:
            is_drop = False
        for i in range(4):
            ny, nx = y+dy[i], x+dx[i]
            if 0 <= ny < R and 0 <= nx < C:
                if not visited[ny][nx] and cave[ny][nx] == 1:
                    deq.append((ny, nx))
                    visited[ny][nx] = cluster
    return is_drop

def drop_cluster(visited, cluster):
    floor = []
    drop_list = []
    for i in range(R):
        for j in range(C):
            if visited[i][j] == cluster:
                drop_list.append((i, j))
                if visited[i+1][j] != cluster:
                    floor.append((i, j))
    drop_height = 1000
    for y, x in floor:
        tmp_drop = 0 
        while True:
            y += 1
            if cave[y][x] == 1 and visited[y][x] != cluster:
                break
            elif y == R-1:
                tmp_drop += 1
                break
            else:
                tmp_drop += 1
        drop_height = min(drop_height, tmp_drop)
    
    for y, x in reversed(drop_list):
        cave[y][x] = 0
        cave[y+drop_height][x] = 1
        
def execute():
    cnt = 1
    visited = [[0] * C for _ in range(R)]
    for y in range(R):
        for x in range(C):
            if cave[y][x] == 1 and not visited[y][x]:
                if check_drop(y, x, cnt, visited):
                    drop_cluster(visited, cnt)
                    return
                else:
                    cnt += 1
    
for i, stick in enumerate(sticks):
    height = R - stick
    if i % 2 == 0:
        x = 0
        while True:
            if cave[height][x] == 1:
                cave[height][x] = 0
                break
            x += 1
            if x == C:
                break
    else:
        x = C-1
        while True:
            if cave[height][x] == 1:
                cave[height][x] = 0
                break
            x -= 1
            if x == -1:
                break
    execute()
    
for i in range(R):
    for j in range(C):
        if cave[i][j] == 1:
            print("x", end="")
        else:
            print(".", end="")
    print()

