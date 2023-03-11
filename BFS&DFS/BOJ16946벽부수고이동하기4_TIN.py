import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
world = [[] for _ in range(n)]

for i in range(n):
    tmp = input().rstrip()
    for j in range(len(tmp)):
        world[i].append(int(tmp[j]))
        
visited = [[0] * m for _ in range(n)]

def dfs(visited, group, y, x):
    visited[y][x] = group
    cnt = 1
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= nx < m and 0 <= ny < n:
            if not visited[ny][nx] and world[ny][nx] == 0:
                cnt += dfs(visited, group, ny, nx)
    return cnt
group_cnt = {}
group_num = 1
result = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if world[i][j] == 0 and not visited[i][j]:
            num = dfs(visited, group_num, i, j)
            group_cnt[group_num] = num
            group_num += 1
for i in range(n):
    for j in range(m):
        if world[i][j] == 1:
            cnt = 1
            around = set()
            for k in range(4):
                nx = j + dx[k]
                ny = i + dy[k]
                if 0 <= nx < m and 0 <= ny < n:
                    if world[ny][nx] == 0:
                        around.add(visited[ny][nx])
            for near in around:
                cnt += group_cnt[near]
            result[i][j] = cnt
for i in range(n):
    for j in range(m):
        print(result[i][j]%10, end="")
    print()