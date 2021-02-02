import sys
from collections import deque
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def dfs(line, v, result):
    for i in line[v]:
        if visited_dfs[i] == 0:
            result.append(i)
            visited_dfs[i] = 1
            dfs(line, i, result)

def bfs(line, v, result):
    q = deque()
    q.append(v)
    result.append(v)

    while q:
        now = q.popleft()
        for i in line[now]:
            if visited_bfs[i] == 0:
                visited_bfs[i] = 1
                result.append(i)
                q.append(i)



N, M, V = map(int, input().split())
result_dfs = []
result_bfs = []
visited_dfs = [0] * (N + 1)
visited_bfs = [0] * (N + 1)
visited_dfs[V] = 1
visited_bfs[V] = 1
result_dfs.append(V)
line = [[] for _ in range(N + 1)]

for _ in range(M):
    start, end = map(int, input().split())
    line[start].append(end)
    line[end].append(start)

for i in range(1, N + 1):
    line[i].sort()

dfs(line, V, result_dfs)
bfs(line, V, result_bfs)

for i in range(len(result_dfs)):
    print(result_dfs[i], end = ' ')
print()
for i in range(len(result_bfs)):
    print(result_bfs[i], end = ' ')
