import sys

input = sys.stdin.readline

def check(x, y):
    success = True
    nx, ny = x+1, y+1
    while nx < n and ny < n:
        if world[ny][nx] == -1:
            success = False
            break
        nx += 1
        ny += 1
    
    nx, ny = x-1, y-1
    while 0 <= nx and 0 <= ny and success:
        if world[ny][nx] == -1:
            success = False
            break
        nx -= 1
        ny -= 1
    
    nx, ny = x+1, y-1
    while nx < n and 0 <= ny and success:
        if world[ny][nx] == -1:
            success = False
            break
        nx += 1
        ny -= 1
    
    nx, ny = x-1, y+1
    while 0 < nx and ny < n and success:
        if world[ny][nx] == -1:
            success = False
            break
        nx -= 1
        ny += 1
    return success

def find_max(x, y, black, cnt):
    global black_cnt, white_cnt
    nx = x + 2
    ny = y
    if black:
        if x >= n-2:
            ny += 1
            nx = 1 if ny % 2 == 0 else 0
        elif y >= n:
            black_cnt = max(black_cnt, cnt)
            return
    else:
        if x >= n-2:
            ny += 1
            nx = 0 if ny % 2 == 0 else 1
        elif y >= n:
            white_cnt = max(white_cnt, cnt)
            return
    if world[y][x] == 1:
        if check(x, y):
            world[y][x] = -1
            find_max(nx, ny, black, cnt+1)
            world[y][x] = 1
            find_max(nx, ny, black, cnt)
        else:
            find_max(nx, ny, black, cnt)
    else:
        find_max(nx, ny, black, cnt)

n = int(input())
world = []
black_cnt = 0
white_cnt = 0
for _ in range(n):
    world.append(list(map(int, input().split())))
find_max(0, 0, 0, 0)
find_max(1, 0, 1, 0)
print(black_cnt + white_cnt)