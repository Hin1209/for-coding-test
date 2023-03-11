import sys
from collections import deque
import heapq
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

node, edge = map(int, input().split())

root = int(input())

INF = 1e9
edges = [[] for _ in range(node+1)]
distance = [INF] * (node+1)

for _ in range(edge):
    start, end, cost = map(int, input().split())
    edges[start].append([end,cost])


def dijkstra(start):
        q = []
        heapq.heappush(q, (0, start))
        distance[start] = 0
        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for i in edges[now]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))
    
dijkstra(root)

for i in range(1, len(distance)):
    if i == root:
        print(0)
    else:
        if distance[i] == INF:
            print("INF")
        else:
            print(distance[i])