import sys
import math

input = sys.stdin.readline

n = int(input())

def calcul_dist(pos1, pos2):
    pow_dist = (pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2
    return math.sqrt(pow_dist)

pos = [0]
INF = 1e9

for _ in range(n):
    x, y = map(float, input().split())
    pos.append((x,y))

dist = []

for i in range(1,n):
    for j in range(i+1, n+1):
        distance = calcul_dist(pos[i], pos[j])
        dist.append((distance, i, j))

parent = [0] * (n+1)
for i in range(1,n+1):
    parent[i] = i

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a
        
dist.sort()
res = 0
for cost, start, end in dist:
    if find_parent(parent, start) != find_parent(parent, end):
        union_parent(parent, start, end)
        res += cost
        
print(res)