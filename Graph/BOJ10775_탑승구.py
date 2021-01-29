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

G = int(input())
P = int(input())
gate = [0] * (G + 1)
park = 0

for i in range(1, G + 1):
    gate[i] = i

for i in range(P):
    dock = find_parent(gate, int(input()))
    # 루트가 0이면 도킹 불가능
    if gate[dock] == 0:
        break
    # 도킹이 가능하면 루트 노드를 작은 것으로 바꿈
    union_group(gate, dock, dock - 1)
    park += 1

print(park)

