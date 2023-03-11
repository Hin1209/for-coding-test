import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

dy = [-1, 0, 1]
res = 0
R, C = map(int, input().split())
world = []
visit = [[0] * C for _ in range(R)]

for _ in range(R):
    tmp = input().rstrip()
    world.append(tmp)

def still(start, y, x):
    if x == C-1:
        return True
    success = False
    for i in range(3):
        ny, nx = y + dy[i], x + 1
        if 0 <= ny < R:
            if world[ny][nx] != 'x' and not visit[ny][nx]:
                visit[ny][nx] = 1
                success = still(start, ny, nx)
                if success:
                    return True
    return False

for i in range(R):
    still(i, i, 0)

res = 0
for i in range(R):
    if visit[i][C-1]:
        res += 1
print(res)
