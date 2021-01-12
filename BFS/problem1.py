from collections import deque

n, m = list(map(int, input().split()))
data = [list(map(int, input().split())) for _ in range(n)]
start = [0, 0]


def bfs(d, s):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque()
    q.append(s)
    while q:
        v = q.popleft()
        for i in range(4):
            ny = v[0] + dy[i]
            nx = v[1] + dx[i]
            if 0 <= nx < m and 0 <= ny < n:
                if d[ny][nx] == 1:
                    q.append([ny, nx])
                    d[ny][nx] = d[v[0]][v[1]] + 1
    return d[n-1][m-1]
print(bfs(data, start))