import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m = map(int, input().split())

parent = [0] * (n+1)

for i in range(n+1):
    parent[i] = i

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a  > b:
        parent[a] = b
    else:
        parent[b] = a
        
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

for i in range(1,m+1):
    start, end = map(int, input().split())
    cycle = False
    if find_parent(parent, start) == find_parent(parent, end):
        cycle = True
        print(i)
        break
    else:
        union_parent(parent, start, end)
if not cycle:
    print(0)