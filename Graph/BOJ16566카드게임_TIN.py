import sys
from bisect import bisect_right

input = sys.stdin.readline

n, m, k = map(int, input().split())

card = list(map(int, input().split()))
card.sort()
rival = list(map(int, input().split()))

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    parent[a] = b

parent = [0] * m
for i in range(m):
    parent[i] = i
    
for i in range(k):
    vs = rival[i]
    index = bisect_right(card, vs)
    target = find_parent(parent, index)
    print(card[target])
    if target == m-1:
        parent[target] = -1
    else:
        union_parent(parent, target, target+1)
