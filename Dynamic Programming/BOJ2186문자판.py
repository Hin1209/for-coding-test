import sys

input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
INF = int(1e9)

n, m, k = map(int, input().split())

world = [input().rstrip() for _ in range(n)]

target = input().rstrip()
length = len(target)

dp = [[[INF] * m for _ in range(n)] for _ in range(length)]

def find_word(y, x, pos):
    if pos ==  length - 1:
        dp[pos][y][x] = 1
        return 1

    if dp[pos][y][x] < INF:
        return dp[pos][y][x]
    
    res = 0
    for d in range(1, k+1):
        for i in range(4):
            ny = y + d * dy[i]
            nx = x + d * dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if world[ny][nx] == target[pos+1]:
                    res += find_word(ny, nx, pos+1)
            
    dp[pos][y][x] = res
    return res 

ans = 0
for i in range(n):
    for j in range(m):
        if world[i][j] == target[0]:
            ans += find_word(i, j, 0)
print(ans)