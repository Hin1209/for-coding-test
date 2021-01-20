import sys
from itertools import combinations
from collections import deque
import copy
def bfs(board, virus):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    safe = 0
    for y, x in virus:
        q = deque()
        q.append([y, x])
        while q:
            v = q.popleft()
            for d in range(4):
                nx = v[1] + dx[d]
                ny = v[0] + dy[d]
                if 0 <= nx < len(board[0]) and 0 <= ny < len(board):
                    if board[ny][nx] == 0:
                        q.append([ny, nx])
                        board[ny][nx] = 2
    for yy in range(len(board)):
        for xx in range(len(board[0])):
            if board[yy][xx] == 0:
                safe += 1
    return safe

n, m = list(map(int, sys.stdin.readline().split()))
board = []
zero = []
virus = []
for i in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            zero.append([i, j])
        elif board[i][j] == 2:
            virus.append([i, j])
chose_wall = list(combinations(zero, 3)) # 벽을 설치하는 모든 경우의 수
max = 0

for i in chose_wall: # 벽을 설치하는 모든 경우의 수에 대해 반복
    tmp = copy.deepcopy(board)
    for j in range(3):
        tmp[i[j][0]][i[j][1]] = 1 # 벽 설치
    tmp_m = bfs(tmp, virus) # 바이러스 전파 후 안전 지대 반환
    if tmp_m > max:
        max = tmp_m
print(max) # 안전 지대가 가장 많이 남는 경우



























