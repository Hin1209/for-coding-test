import sys

input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_group(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())
graph = []
parent = [0] * (N + 1)

for i in range(1, N + 1):
    parent[i] = i

for i in range(M):
    a, b = map(int, input().split())
    graph.append((a, b))

graph.sort()

for i in range(len(graph)):
    u, v = graph[i]
    union_group(parent, u, v)

result = set()

for i in range(1, len(parent)):
    result.add(find_parent(parent, i))

print(len(result))