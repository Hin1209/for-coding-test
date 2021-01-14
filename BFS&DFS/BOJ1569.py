import sys
from collections import deque

m, n, h = list(map(int, sys.stdin.readline().split()))
box = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]
tmp_box = []
check_zero = 0
visited = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]
q = deque()
for i in range(h):
    for j in range(n):
        box[i][j] = list(map(int, sys.stdin.readline().split()))

for z in range(h):
    for y in range(n):
        for x in range(m):
            if box[z][y][x] == 1:
                q.append([z, y, x])
                visited[z][y][x] = 1
            elif box[z][y][x] == 0:
                check_zero += 1
time = 0
execpt = 0
if check_zero == 0:
    execpt = 1
while q:
    if execpt == 1:
        break
    z, y, x = q.popleft()
    if z > 0:
        if visited[z-1][y][x] == 0 and box[z-1][y][x] == 0:
            visited[z-1][y][x] = visited[z][y][x] + 1
            time = max(time, visited[z-1][y][x])
            box[z-1][y][x] = 1
            q.append([z-1, y, x])
            check_zero -= 1
    if z < h-1:
        if visited[z+1][y][x] == 0 and box[z+1][y][x] == 0:
            visited[z+1][y][x] = visited[z][y][x] + 1
            time = max(time, visited[z+1][y][x])
            box[z+1][y][x] = 1
            q.append([z+1, y, x])
            check_zero -= 1
    if y > 0:
        if visited[z][y-1][x] == 0 and box[z][y-1][x] == 0:
            visited[z][y-1][x] = visited[z][y][x] + 1
            time = max(time, visited[z][y-1][x])
            box[z][y-1][x] = 1
            q.append([z, y-1, x])
            check_zero -= 1
    if y < n-1:
        if visited[z][y+1][x] == 0 and box[z][y+1][x] == 0:
            visited[z][y+1][x] = visited[z][y][x] + 1
            time = max(time, visited[z][y+1][x])
            box[z][y+1][x] = 1
            q.append([z, y+1, x])
            check_zero -= 1
    if x > 0:
        if visited[z][y][x-1] == 0 and box[z][y][x-1] == 0:
            visited[z][y][x-1] = visited[z][y][x] + 1
            time = max(time, visited[z][y][x-1])
            box[z][y][x-1] = 1
            q.append([z, y, x-1])
            check_zero -= 1
    if x < m-1:
        if visited[z][y][x+1] == 0 and box[z][y][x+1] == 0:
            visited[z][y][x+1] = visited[z][y][x] + 1
            time = max(time, visited[z][y][x+1])
            box[z][y][x+1] = 1
            q.append([z, y, x+1])
            check_zero -= 1

if execpt == 1:
    print(0)
else:
    if check_zero != 0:
        print(-1)
    else:
        print(time-1)