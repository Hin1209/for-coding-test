import sys
sys.setrecursionlimit(10**7)

input = sys.stdin.readline

n, m = map(int, input().split())

world = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for _ in range(n):
    world.append(list(map(int, input().split())))

time = 0

outside = [[False for _ in range(m)] for _ in range(n)]

def check_outside(y, x):
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= nx < m and 0 <= ny < n:
            if world[ny][nx] == 0 and outside[ny][nx] == False:
                outside[ny][nx] = True
                check_outside(ny, nx)
                
def remove_cheese():
    remove = []
    for y in range(n):
        for x in range(m):
            if world[y][x] == 1:
                count = 0
                for k in range(4):
                    ny, nx = y + dy[k], x + dx[k]
                    if world[ny][nx] == 0 and outside[ny][nx]:
                        count += 1
                if count >= 2:
                    remove.append((y, x))
    for ry, rx in remove:
        world[ry][rx] = 0

def exist_cheese():
    for y in range(n):
        for x in range(m):
            if world[y][x] == 1:
                return True
    return False

while exist_cheese():
    check_outside(0,0)
    remove_cheese()
    outside = [[False for _ in range(m)] for _ in range(n)]
    time += 1

print(time)