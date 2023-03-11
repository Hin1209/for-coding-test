import sys

input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
world = [[] for _ in range(10)]
tmp = [[False] * 10 for _ in range(10)]
for i in range(10):
    string = input().rstrip()
    for j in string:
        if j == "O":
            world[i].append(True)
        else:
            world[i].append(False)

def switch(y, x):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 10 and 0 <= ny < 10:
            if tmp[ny][nx]:
                tmp[ny][nx] = False
            else:
                tmp[ny][nx] = True
    if tmp[y][x]:
        tmp[y][x] = False
    else:
        tmp[y][x] = True

def copy():
    for i in range(10):
        for j in range(10):
            tmp[i][j] = world[i][j]

def isDark():
    for j in range(10):
        if tmp[9][j]:
            return False
    return True

res = 1e9
for state in range(1 << 10):
    cnt = 0
    copy()
    for i in range(10):
        if state & (1 << i):
            cnt += 1
            switch(0, i)
    for i in range(1,10):
        for j in range(10):
            if tmp[i-1][j]:
                cnt += 1
                switch(i,j)
    if isDark():
        res = min(res, cnt)
if res == 1e9:
    print(-1)
else:
    print(res)