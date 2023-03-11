import sys
from collections import deque
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def remove_door(key):
    result = []
    for i in range(h+2):
        for j in range(w+2):
            if not world[i][j].islower() and world[i][j].lower() == key:
                world[i][j] = "."
                for k in range(4):
                    nx = j + dx[k]
                    ny = i + dy[k]
                    if 0 <= nx < w+2 and 0 <= ny < h+2:
                        if visited[ny][nx]:
                            result.append((i, j))
                            break
    return result
result = []
t = int(input())
for _ in range(t):
    h, w = map(int, input().split())
    world = [[] for _ in range(h+2)]
    world[0] = ["."] * (w+2)
    world[h+1] = ["."] * (w+2)
    for i in range(1,h+1):
        world[i].append(".")
        tmp = input().rstrip()
        for j in tmp:
            world[i].append(j)
        world[i].append(".")
    keys = input().rstrip()
    visited = [[False] * (w+2) for _ in range(h+2)]
    visited[0][0] = True
    for key in keys:
        remove_door(key)
    deq = deque()
    deq.append((0,0))
    res = 0
    while deq:
        y, x = deq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < w+2 and 0 <= ny < h+2:
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    if world[ny][nx] == ".":
                        deq.append((ny, nx))
                    elif world[ny][nx] == "$":
                        world[ny][nx] = "."
                        res += 1
                        deq.append((ny,nx))
                    elif world[ny][nx].islower():
                        open = remove_door(world[ny][nx])
                        for pos in open:
                            deq.append((pos[0], pos[1]))
                        deq.append((ny,nx))
    result.append(res)
for i in result:
    print(i)