import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n = int(input())
ants = []

for _ in range(n):
    ants.append(int(input()))
    
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    
dist = [INF] * (n+1)
next_cave = [0] * (n+1)
h = []
heapq.heappush(h, (0, 1))
dist[1] = 0
    
while h:
    cost, now = heapq.heappop(h)
    for next_node, c in graph[now]:
        next_cost = cost + c
        if dist[next_node] > next_cost:
            dist[next_node] = next_cost
            heapq.heappush(h, (next_cost, next_node))
            next_cave[next_node] = now
    
def find_last(start, energy):
    now = start
    while energy:
        next_node = next_cave[now]
        energy -= (dist[now] - dist[next_node])
        if energy < 0:
            break
        now = next_node
    return now
    
for i in range(n):
    start = i+1
    energy = ants[i]
    if energy >= dist[start]:
        print(1)
    else:
        print(find_last(start, energy))