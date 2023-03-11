import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

import heapq

n = 6
edge =[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
INF = int(1e9)

def solution(n, edge):
    h = []
    dist = [INF] * (n+1)
    dist[1] = 0
    dist[0] = 0
    graph = [[] for _ in range(n+1)]
    for start, end in edge:
        graph[start].append(end)
        graph[end].append(start)
    heapq.heappush(h, (0, 1))
    while h:
        cost, node = heapq.heappop(h)
        for next in graph[node]:
            if dist[next] > cost + 1:
                dist[next] = cost + 1
                heapq.heappush(h, (cost+1, next))
    max_length = max(dist)
    cnt = 0
    print(max_length)
    for i in range(1, n+1):
        if dist[i] == max_length:
           cnt += 1
    print(cnt)
    
solution(n, edge) 