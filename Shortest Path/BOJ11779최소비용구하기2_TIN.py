import sys
import heapq

input = sys.stdin.readline

num_city = int(input())
num_bus = int(input())

graph = [[] for _ in range(num_city+1)]
INF = 1e9
dist = [INF] * (num_city + 1)

for _ in range(num_bus):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))
    
start_city, end_city = map(int, input().split())

def dijkstra(start, end):
    q = [] 
    dist[start] = 0
    heapq.heappush(q,(0, start, [start]))
    while q:
        total_cost, node, node_list = heapq.heappop(q)
        if node == end:
            return total_cost, node_list
        if dist[node] < total_cost:
            continue
        for next_node, cost in graph[node]:
            if total_cost + cost < dist[next_node]:
                tmp = []
                for i in node_list:
                    tmp.append(i)
                dist[next_node] = total_cost + cost
                tmp.append(next_node)
                heapq.heappush(q, (total_cost + cost, next_node, tmp))
                
cost, city_list = dijkstra(start_city, end_city)
print(cost)
print(len(city_list))
for i in city_list:
    print(i, end = " ")