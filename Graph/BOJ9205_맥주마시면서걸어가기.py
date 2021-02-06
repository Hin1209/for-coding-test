import sys
import heapq

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


T = int(input())

for _ in range(T):
    n = int(input())
    start = tuple(map(int, input().split()))
    parent = [0] * (n + 2)
    beer = [start]
    edge = []
    h = []

    for i in range(n + 2):
        parent[i] = i

    for i in range(n):
        x, y = map(int, input().split())
        beer.append((x, y))

    festival = tuple(map(int, input().split()))
    beer.append(festival)

    for i in range(n + 1):
        for j in range(i + 1, n + 2):
            cost = abs(beer[i][0] - beer[j][0]) + abs(beer[i][1] - beer[j][1])
            heapq.heappush(edge, (cost, i, j))


    while edge:
        distance, st, ed = heapq.heappop(edge)
        if find_parent(parent, st) != find_parent(parent, ed):
            if distance > 1000:
                continue
            else:
                union_group(parent, st, ed)

    if find_parent(parent, 0) == find_parent(parent, n + 1):
        print("happy")
    else:
        print("sad")






