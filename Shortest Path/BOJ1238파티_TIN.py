import sys
import heapq

input = sys.stdin.readline

n, m, x = map(int, input().split())
INF = 1e9
graph = [[] for _ in range(n+1)]

for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append((cost, end))

def dijkstra(start,n):
    q = []
    heapq.heappush(q, (0, start))
    dist = [INF] * (n+1)
    dist[start] = 0
    while q:
        cost, node = heapq.heappop(q)
        if dist[node] < cost:
            continue
        for c, n in graph[node]:
            if cost + c < dist[n]:
                dist[n] = cost + c
                heapq.heappush(q, (cost + c, n))
    return dist

count = 0
for i in range(1,n+1):
    if i == x: continue
    go_party = dijkstra(x,n)[i]
    back_home = dijkstra(i,n)[x]
    if count < go_party + back_home:
        count = go_party + back_home
print(count)