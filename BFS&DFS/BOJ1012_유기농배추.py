import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

T = int(input())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(array, x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= len(array[0]) or ny < 0 or ny >= len(array):
            continue
        else:
            if array[ny][nx] == 1:
                array[ny][nx] = 0
                dfs(array, nx, ny)

for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0 for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1

    cnt = 0

    for i in range(N):
        for j in range(M):
            if field[i][j] == 1:
                field[i][j] = 0
                dfs(field, j, i)
                cnt += 1

    print(cnt)
