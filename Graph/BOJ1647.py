import sys

input = sys.stdin.readline

def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())
house = [0] * (N + 1)
road = []
result = 0

for i in range(M):
    a, b, cost = map(int, input().split())
    road.append((cost, a, b))

road.sort()
for i in range(1, N + 1):
    house[i] = i
max_cost = 0
for edge in road:
    cost, a, b = edge
    if find_parent(house, a) != find_parent(house, b):
        union_parent(house, a, b)
        result += cost
        max_cost = max(max_cost, cost)

print(result - max_cost)
