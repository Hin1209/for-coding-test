from collections import deque

n, l, r = list(map(int, input().split()))
country = [list(map(int, input().split())) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

q = deque()
relieve = [[0 for _ in range(n)] for _ in range(n)]
circular = 0
while True:
    if n == 1:
        break
    q.append([0, 0])
    visited = [[0 for _ in range(n)] for _ in range(n)]
    visited[0][0] = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[ny][nx] == 0:
                    q.append([ny, nx])
                    visited[ny][nx] = 1
                if l <= abs(country[y][x] - country[ny][nx]) <= r:
                    relieve[y][x] = 1
                    relieve[ny][nx] = 1
    vi = deque()
    stop = 0
    for ii in range(n):
        for jj in range(n):
            if relieve[ii][jj] == 1:
                vi.append([ii, jj])
                link = set()
                link.add((ii, jj))
                result = 0
                relieve[ii][jj] = 0
                while vi:
                    vy, vx = vi.popleft()
                    for dr in range(4):
                        vnx = vx + dx[dr]
                        vny = vy + dy[dr]
                        if 0 <= vnx < n and 0 <= vny < n:
                            if relieve[vny][vnx] == 1:
                                vi.append([vny, vnx])
                                relieve[vny][vnx] = 0
                                link.add((vny, vnx))
                for ky, kx in link:
                    result += country[ky][kx]
                result = int(result/len(link))
                for cy, cx in link:
                    country[cy][cx] = result
            else:
                stop += 1
    if stop == n * n:
        break
    circular += 1
print(circular)


