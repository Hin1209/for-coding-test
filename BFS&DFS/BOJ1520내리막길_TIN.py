import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

m, n = map(int, input().split())
world = []
dp = [[0] * n for _ in range(m)]
visit = [[0] * n for _ in range(m)]
visit[m-1][n-1] = 1
dp[m-1][n-1] = 1
for i in range(m):
    world.append(list(map(int, input().split())))

def move(x, y):
    cnt = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if world[ny][nx] < world[y][x]:
                if dp[ny][nx]:
                    cnt += dp[ny][nx]
                else:
                    if not visit[ny][nx]:
                        visit[ny][nx] = 1
                        cnt += move(nx, ny)
                    else:
                        continue
    dp[y][x] = cnt
    return cnt

print(move(0,0))