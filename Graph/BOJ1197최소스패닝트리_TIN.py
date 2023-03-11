import sys

input = sys.stdin.readline

num_node, num_edge = map(int, input().split())


parent = [0] * (num_node + 1)
edges = []

for i in range(1, num_node + 1):
    parent[i] = i
    
for _ in range(num_edge):
    start, end, cost = map(int, input().split())
    edges.append((cost, start, end))
edges.sort()
    
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a
        
result = 0
        
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(result)