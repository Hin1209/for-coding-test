from collections import deque
import sys

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, k = list(map(int, sys.stdin.readline().split()))
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
s, x, y = list(map(int, sys.stdin.readline().split()))

virus = []

for i in range(n):
    for j in range(n):
        if board[i][j] != 0:
            virus.append([board[i][j], i, j, 0])

virus.sort()
q_virus = deque(virus)
while q_virus:
    size_v, yy, xx, time = q_virus.popleft()
    if time == s:
        break
    for i in range(4):
        nx = xx + dx[i]
        ny = yy + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        else:
            if board[ny][nx] == 0:
                board[ny][nx] = size_v
                q_virus.append([size_v, ny, nx, time+1])
print(board[x-1][y-1])