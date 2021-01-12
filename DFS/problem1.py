from collections import deque


def dfs(x, y, visited):
    global data
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque([x, y])
    visited[x][y] = 1
    data[x][y] = 1
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < n and 0 <= yy < m:
            if data[xx][yy] == 0 and visited[xx][yy] == 0:
                q.append([xx, yy])
                visited[xx][yy] = 1
                data[xx][yy] = 1
                dfs(xx, yy, visited)
call = 0
count = 0
n, m = list(map(int, input().split()))
data = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if data[i][j] == 0:
            dfs(i, j, visited)
            count += 1

print(count)
