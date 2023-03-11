import sys
from collections import deque
input = sys.stdin.readline

r, c, t = map(int, input().split())

world = []
dx = [1,0,-1,0]
dy = [0,1,0,-1]

for _ in range(r):
    world.append(list(map(int, input().split())))

tmp_world = [[0] * c for _ in range(r)]
pos_air = []

for i in range(r):
    if world[i][0] == -1:
        pos_air.append(i)

def diffuse():
    for y in range(r):
        for x in range(c):
            if world[y][x] > 0:
                count = 0
                for k in range(4):
                        ny = y + dy[k]
                        nx = x + dx[k]
                        if 0 <= nx < c and 0 <= ny < r:
                            if world[ny][nx] != -1:
                                count += 1
                                tmp_world[ny][nx] += world[y][x] // 5
                world[y][x] -= world[y][x] // 5 * count
    for y in range(r):
        for x in range(c):
            world[y][x] += tmp_world[y][x]
                
    for y in range(r):
        for x in range(c):
            tmp_world[y][x] = 0
            
def move():
    up = pos_air[0]
    down = pos_air[1]
    deq = deque()
    deq.append((up,1,0))
    while deq:
        y, x, amount = deq.popleft()
        if y == up and x < c-1:
            deq.append((up,x+1,world[y][x]))
            world[y][x] = amount
        elif 0 < y <= up and x == c-1:
            deq.append((y-1,x,world[y][x]))
            world[y][x] = amount
        elif y == 0 and 0 < x:
            deq.append((0,x-1,world[y][x]))
            world[y][x] = amount
        elif 0 <= y < up and x == 0:
            if y == up-1:
                world[y][x] = amount
            else:
                deq.append((y+1,x,world[y][x]))
                world[y][x] = amount
                
    deq = deque()
    deq.append((down,1,0))
    while deq:
        y, x, amount = deq.popleft()
        if y == down and x < c-1:
            deq.append((down,x+1,world[y][x]))
            world[y][x] = amount
        elif down <= y < r-1 and x == c-1:
            deq.append((y+1,x,world[y][x]))
            world[y][x] = amount
        elif y == r-1 and 0 < x:
            deq.append((r-1,x-1,world[y][x]))
            world[y][x] = amount
        elif down <= y < r and x == 0:
            if y == down+1:
                world[y][x] = amount
            else:
                deq.append((y-1,x,world[y][x]))
                world[y][x] = amount

time = 0
while time < t:
    time += 1
    diffuse()
    move()
sum = 0
for i in range(r):
    for j in range(c):
        sum += world[i][j]
print(sum + 2)
