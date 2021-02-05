import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(board, y, x, visited, cnt):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < len(board) and ny >= 0 and ny < len(board):
            if board[ny][nx] == 1 and visited[ny][nx] == 0:
                visited[ny][nx] = cnt
                dfs(board, ny, nx, visited, cnt)

N = int(input())

board = [[] for _ in range(N)]
visited = [[0] * N for _ in range(N)]
cnt = 1
for i in range(N):
    tmp = input().rstrip()
    for j in range(N):
        board[i].append(int(tmp[j]))

for i in range(N):
    for j in range(N):
        if board[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = cnt
            dfs(board, i, j, visited, cnt)
            cnt += 1

result = cnt - 1
house_num = []

for i in range(1, cnt):
    tmp = 0
    for j in range(N):
        for k in range(N):
            if visited[j][k] == i:
                tmp += 1
    house_num.append(tmp)

house_num.sort()
print(result)
for i in range(len(house_num)):
    print(house_num[i])