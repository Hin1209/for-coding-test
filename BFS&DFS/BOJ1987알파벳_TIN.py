import sys
from collections import deque

input = sys.stdin.readline

r, c = map(int, input().split())
world = []
for _ in range(r):
    world.append(input().rstrip())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

count = 0

status = [True] * (ord("Z") + 1)

def dfs(y, x, cnt):
    global count
    if count < cnt:
        count = cnt
    for i in range(4):
        nx =  x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < c and 0 <= ny < r:
            alpha = ord(world[ny][nx])
            if status[alpha]:
                status[alpha] = False
                cnt += 1
                dfs(ny, nx, cnt)
                status[alpha] = True
                cnt -= 1
start = ord(world[0][0])
status[start] = False
dfs(0, 0, 1)
print(count)