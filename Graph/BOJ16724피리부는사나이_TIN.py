import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())

world = []

for _ in range(n):
    tmp = input().rstrip()
    world.append(tmp)

parent = [0] * (n*m)
for i in range(n*m):
    parent[i] = i
graph = [0] * (n*m)
for i in range(n):
    for j in range(m):
        if world[i][j] == "D":
            graph[i*m+j] = i*m+j+m
        elif world[i][j] == "L":
            graph[i*m+j] = i*m+j-1
        elif world[i][j] == "R":
            graph[i*m+j] = i*m+j+1
        elif world[i][j] == "U":
            graph[i*m+j] = i*m+j-m

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

for i in range(n*m):
    next = graph[i]
    if find_parent(parent, i) != find_parent(parent, next):
        union_parent(parent, i, next)

res = set()
for i in range(n*m):
    tmp = find_parent(parent, i)
    res.add(tmp)
print(len(res))