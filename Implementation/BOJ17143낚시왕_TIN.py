import sys

input = sys.stdin.readline

r, c, m = map(int, input().split())

world = [[0] * c for _ in range(r)]

shark = [0] * (10001)
for _ in range(m):
    y, x, v, d, s = map(int, input().split())
    shark[s] = [y-1,x-1,v,d]
    world[y-1][x-1] = s

def move_shark(y, x, v, d):
    height = 2*(r-1)
    width = 2*(c-1)
    if d == 1:
        move = v % height
        if move > y + r - 1:
            y = 2*(r-1) + y - move
            d = 1
        elif y < move:
            y =  move - y
            d = 2
        elif y >= move:
            y = y - move
            d = 1
    elif d == 2:
        move = v % height
        if move > 2*(r-1) - y:
            y = move - (2*(r-1) - y)
            d = 2
        elif move > r - 1 - y:
            y = 2*(r-1) - y - move
            d = 1
        elif move <= r - 1 - y:
            y = y + move
            d = 2 
    elif d == 3:
        move = v % width
        if move > 2*(c-1) - x:
            x = move - (2*(c-1) - x)
            d = 3
        elif move > c - 1 - x:
            x = 2*(c-1) - x - move
            d = 4
        elif move <= c - 1 - x:
            x = x + move
            d = 3
    elif d == 4:
        move = v % width
        if move > x + c - 1:
            x = 2*(c-1) + x - move
            d = 4
        elif x < move:
            x =  move - x
            d = 3
        elif x >= move:
            x = x - move
            d = 4
    return y, x, d

res = 0
for i in range(c):
    check = 0
    while check < r and world[check][i] == 0:
        check += 1
    if check != r:
        res += world[check][i]
        shark[world[check][i]] = 0
        world[check][i] = 0
    for j in range(1,10001):
        if shark[j] != 0:
            y,x,v,d = shark[j]
            ny,nx,nd = move_shark(y,x,v,d)
            if world[ny][nx] != 0 and world[ny][nx] < j:
                shark[world[ny][nx]] = 0    
            if world[y][x] == j:
                world[y][x] = 0
            world[ny][nx] = j
            shark[j] = [ny,nx,v,nd]
print(res)