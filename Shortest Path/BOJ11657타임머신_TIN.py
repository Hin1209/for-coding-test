import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
road = [[] for _ in range(n+1)]
costs = [1e9] * (n+1)
costs[1] = 0

for _ in range(m):
    start, end, time = map(int, input().split())
    road[start].append((time,end))
    

possible = False

for i in range(len(road)):
    road[i].sort()
for i in range(1,n+1):
    for j in range(1,n+1):
        for cost, next in road[j]:
            if costs[next] == 1e9 and costs[j] == 1e9:
                continue
            if costs[next] > costs[j] + cost:
                costs[next] = costs[j] + cost
                if i == n:
                    possible = True
            
if possible:
    print(-1)
else:
    for i in range(2, n+1):
        if costs[i] == 1e9:
            print(-1)
        else:
            print(costs[i])