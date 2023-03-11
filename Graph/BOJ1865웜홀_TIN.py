import sys
from collections import deque

input = sys.stdin.readline

test = int(input())

for _ in range(test):
    n, m, w = map(int, input().split())
    road = [[] for _ in range(n+1)]
    costs = [1e9] * (n+1)
    costs[1] = 0
    possible = False
    for _ in range(m):
        start, end, time = map(int, input().split())
        road[start].append((time,end))
        road[end].append((time,start))
    for _ in range(w):
        start, end, time = map(int, input().split())
        road[start].append((-time,end))
    for i in range(len(road)):
        road[i].sort()
    for i in range(1,n+1):
        for j in range(1,n+1):
            for cost, next in road[j]:
                if costs[next] > costs[j] + cost:
                    costs[next] = costs[j] + cost
                    if i == n:
                        possible = True
                
    if possible:
        print("YES")
    else:
        print("NO")
        
