from collections import deque

n, l, r = list(map(int, input().split()))
country = [list(map(int, input().split())) for _ in range(n)]

q = deque()
relieve = [[0 for _ in range(n)] for _ in range(n)]
circular = 0
while True:
    if n == 1:
        break
    cnt = 0
    q.append([0, 0])
    visited = [[0 for _ in range(n)] for _ in range(n)]
    visited[0][0] = 1
    while q:
        y, x = q.popleft()
        if y > 0:
            if l <= abs(country[y][x] - country[y-1][x]) <= r:
                if relieve[y][x] == 0 and relieve[y-1][x] == 0:
                    cnt += 1
                    relieve[y][x] = cnt
                if relieve[y][x] != relieve[y-1][x] and relieve[y][x] != 0 and relieve[y-1][x] != 0:
                    relieve[y-1][x] = min(relieve[y][x], relieve[y-1][x])
                    relieve[y][x] = min(relieve[y][x], relieve[y-1][x])
                    cnt = min(relieve[y][x], relieve[y-1][x])
            if visited[y-1][x] == 0:
                q.append([y-1, x])
                visited[y-1][x] = 1
        if y < n-1:
            if l <= abs(country[y][x] - country[y+1][x]) <= r:
                if relieve[y][x] == 0 and relieve[y + 1][x] == 0:
                    cnt += 1
                    relieve[y][x] = cnt
                if relieve[y][x] != relieve[y+1][x] and relieve[y][x] != 0 and relieve[y+1][x] != 0:
                    relieve[y+1][x] = min(relieve[y][x], relieve[y+1][x])
                    relieve[y][x] = min(relieve[y][x], relieve[y+1][x])
                    cnt = min(relieve[y][x], relieve[y+1][x])
            if visited[y+1][x] == 0:
                q.append([y+1, x])
                visited[y+1][x] = 1
        if x > 0:
            if l <= abs(country[y][x] - country[y][x-1]) <= r:
                if relieve[y][x] == 0 and relieve[y][x-1] == 0:
                    cnt += 1
                    relieve[y][x] = cnt
                if relieve[y][x] != relieve[y][x-1] and relieve[y][x] != 0 and relieve[y][x-1] != 0:
                    relieve[y-1][x] = min(relieve[y][x], relieve[y-1][x])
                    relieve[y][x] = min(relieve[y][x], relieve[y-1][x])
                    cnt = min(relieve[y][x], relieve[y][x-1])
            if visited[y][x-1] == 0:
                q.append([y, x-1])
                visited[y][x-1] = 1
        if x < n-1:
            if l <= abs(country[y][x] - country[y][x+1]) <= r:
                if relieve[y][x] == 0 and relieve[y][x+1] == 0:
                    cnt += 1
                    relieve[y][x] = cnt
                if relieve[y][x] != relieve[y][x+1] and relieve[y][x] != 0 and relieve[y][x+1] != 0:
                    relieve[y][x+1] = min(relieve[y][x], relieve[y][x+1])
                    relieve[y][x] = min(relieve[y][x], relieve[y][x+1])
                    cnt = min(relieve[y][x], relieve[y][x+1])
            if visited[y][x+1] == 0:
                q.append([y, x+1])
                visited[y][x+1] = 1
    vi = deque()
    stop = 0
    if cnt == 0:
        break
    for i in range(1, cnt+1):
        for ii in range(n):
            for jj in range(n):
                if relieve[ii][jj] == i:
                    vi.append([ii, jj])
                    link = set()
                    link.add((ii, jj))
                    result = 0
                    relieve[ii][jj] = 0
                    while vi:
                        vy, vx = vi.popleft()
                        if vy > 0:
                            if relieve[vy-1][vx] == i:
                                vi.append([vy-1, vx])
                                relieve[vy-1][vx] = 0
                                link.add((vy-1, vx))
                        if vy < n-1:
                            if relieve[vy+1][vx] == i:
                                vi.append([vy+1, vx])
                                relieve[vy+1][vx] = 0
                                link.add((vy+1, vx))
                        if vx > 0:
                            if relieve[vy][vx-1] == i:
                                vi.append([vy, vx-1])
                                relieve[vy][vx-1] = 0
                                link.add((vy, vx-1))
                        if vx < n-1:
                            if relieve[vy][vx+1] == i:
                                vi.append([vy, vx+1])
                                relieve[vy][vx+1] = 0
                                link.add((vy, vx+1))
                    for ky, kx in link:
                        result += country[ky][kx]
                    result = int(result/len(link))
                    for cy, cx in link:
                        country[cy][cx] = result
                else:
                    stop += 1
    circular += 1
print(circular)


# 5 10 20
# 10 15 30 40 15
# 15 30 60 55 20
# 30 20 50 45 40
# 10 15 40 5 10
# 20 5 10 20 15

# 4 10 50
# 10 100 20 90
# 80 100 60 70
# 70 20 30 40
# 50 20 100 10