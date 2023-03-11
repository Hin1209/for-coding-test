import sys
import heapq
input = sys.stdin.readline

n, e = map(int, input().split())
INF = int(1e9)
dist1 = [INF] * (n+1)
dist2 = [INF] * (n+1)
dist3 = [INF] * (n+1)
graph = [[] for _ in range(n+1)]
dist1[1] = 0

for i in range(e):
    start, end, cost = map(int, input().split())
    graph[start].append((cost, end))
    graph[end].append((cost, start))

v1, v2 = map(int, input().split())
dist2[v1] = 0
dist3[v2] = 0

def dijkstra(start, dist):
    heap = []
    heapq.heappush(heap, (0, start))
    dist[start] = 0
    while heap:
        cost, now = heapq.heappop(heap)
        if dist[now] < cost:
            continue
        for c, next in graph[now]:
            if cost + c < dist[next]:
                dist[next] = cost + c
            heapq.heappush(heap, (cost + c, next))

dijkstra(1, dist1)
dijkstra(v1, dist2)
dijkstra(v2, dist3)

first = dist1[v1] + dist2[v2] + dist3[n]
second = dist1[v2] + dist3[v1] + dist2[n]

if first >= INF and second >= INF: print(-1)
else: print(min(first, second))

