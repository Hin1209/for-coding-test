import sys
from collections import deque

m, n, h = list(map(int, sys.stdin.readline().split()))
box = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]
tmp_box = []
check_zero = 0 # 익지 않은 토마토의 개수
visited = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]
q = deque()
for i in range(h):
    for j in range(n):
        box[i][j] = list(map(int, sys.stdin.readline().split()))

for z in range(h):
    for y in range(n):
        for x in range(m):
            if box[z][y][x] == 1:
                q.append([z, y, x]) # q에 익은 토마토 위치 추가
                visited[z][y][x] = 1 # visited에 시간 저장
            elif box[z][y][x] == 0:
                check_zero += 1
time = 0
execpt = 0
if check_zero == 0: # 안익은 토마토가 없으면 예외 처리
    execpt = 1
while q:
    if execpt == 1:
        break
    z, y, x = q.popleft() # 저장된 z, y, x 제거
    if z > 0: # 다음 좌표에 방문한 적이 없고 익지 않은 토마토가 있는 경우 시간을 +1 해주고 q에 좌표 추가
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
    print(0) # 처음부터 다 익은 상태
else:
    if check_zero != 0:
        print(-1) # 토마토가 다 익을 수 없는 상황
    else:
        print(time-1) # 처음 시간이 1부터 시작했으므로 1을 빼줘야함