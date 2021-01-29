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
            # virus 리스트에 바이러스의 크기, 위치, 마지막으로 시간을 0으로 해서 담음(초기 상태)
            virus.append([board[i][j], i, j, 0])

virus.sort()
q_virus = deque(virus)
while q_virus:
    size_v, yy, xx, time = q_virus.popleft()
    # 문제에서 요구한 시간이 되면 반복문 종료
    if time == s:
        break
    # 바이러스 위치에서 상하좌우 검사
    for i in range(4):
        nx = xx + dx[i]
        ny = yy + dy[i]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        else:
            # 바이러스 주변에 빈 공간이 있으면 바이러스 전파.
            if board[ny][nx] == 0:
                board[ny][nx] = size_v
                # 시간을 +1 해줌
                q_virus.append([size_v, ny, nx, time+1])
# board의 인덱스가 0부터 시작하므로 -1을 해줌
print(board[x-1][y-1])