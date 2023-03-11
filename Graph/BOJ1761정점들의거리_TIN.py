import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
distance = [0] * (n+1) 
parent = [[0] * 20 for _ in range(n+1)]
depth = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))
    graph[end].append((start, cost))

def set_tree(now, dist, par, level):
    depth[now] = level
    parent[now][0] = par
    distance[now] = dist
    for i in range(1,20):
        parent[now][i] = parent[parent[now][i-1]][i-1]
    for next, cost in graph[now]:
        if next == par:
            continue
        set_tree(next, dist + cost, now, level + 1)
    
def find_path(a, b):
    if a == 1 and b == 1:
        return 1
    if depth[a] < depth[b]:
        a, b = b, a
    target = a
    compare = b
    if depth[target] != depth[compare]:
        for i in range(19, -1, -1):
            if depth[parent[target][i]] >= depth[compare]:
                target = parent[target][i] 
    res = target
    if target != compare:
        for i in range(19, -1, -1):
            if parent[target][i] != parent[compare][i]:
                target = parent[target][i]
                compare = parent[compare][i]
            res = parent[target][i]
    return res

set_tree(1,0,1,1)
m = int(input())
res = []
for _ in range(m):
    start, end = map(int, input().split())
    common_par = find_path(start, end)
    res.append(distance[start] + distance[end] - 2 * distance[common_par])
for i in res:
    print(i)
