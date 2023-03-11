import sys
import heapq

input = sys.stdin.readline

subin, bro = map(int, input().split())

INF = 1e9
cost = [INF] * 100001

cost[subin] = 0

heap = []
heapq.heappush(heap, (0, subin))
count = 1

while heap:
    c, pos = heapq.heappop(heap)
    if pos+1 < len(cost) and pos+1 == bro:
        if cost[bro] == c+1:
            count += 1
        elif cost[bro] > c+1:
            count = 1
            cost[bro] = c+1
    elif pos+1 < len(cost) and cost[pos+1] >= c+1:
        cost[pos+1] = c+1
        heapq.heappush(heap, (c+1, pos+1))
    if pos*2 < len(cost) and pos*2 == bro:
        if cost[bro] == c+1:
            count += 1
        elif cost[bro] > c+1:
            count = 1
            cost[bro] = c+1
    elif pos*2 < len(cost) and cost[pos*2] >= c+1:
        cost[pos*2] = c+1
        heapq.heappush(heap, (c+1, pos*2))
    if pos-1 >=0 and pos-1 == bro:
        if cost[bro] == c+1:
            count += 1
        elif cost[bro] > c+1:
            count = 1
            cost[bro] = c+1
    elif pos-1 >= 0 and cost[pos-1] >= c+1:
        cost[pos-1] = c+1
        heapq.heappush(heap, (c+1, pos-1))
            
print(cost[bro])
print(count)