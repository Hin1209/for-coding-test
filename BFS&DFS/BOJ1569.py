import sys
from collections import deque

m, n, h = list(map(int, sys.stdin.readline().split()))
direction = [(0, 1, 0), (1, 0, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]
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
while q:
    z, y, x = q.popleft()
    for dz, dy, dx in direction:
        nz, ny, nx = z + dz, y + dy, x + dx
        if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m:
            if visited[nz][ny][nx] == 0 and box[nz][ny][nx] == 0:
                visited[nz][ny][nx] = visited[z][y][x]+1
                time = max(time, visited[nz][ny][nx])
                box[nz][ny][nx] = 1
                q.append([nz, ny, nx])
                check_zero -= 1

if check_zero:
    print(-1)
else:
    print(time-1)