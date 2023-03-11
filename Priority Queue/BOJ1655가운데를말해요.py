import sys
import heapq

input = sys.stdin.readline

n = int(input())

high = []
low = []
for _ in range(n): 
    tmp = int(input())
    if len(low) > 0 and len(high) > 0:
        max_low = -low[0]
        min_high = high[0]
        if tmp < max_low:
            heapq.heappush(low, -tmp)
        elif tmp > min_high:
            heapq.heappush(high, tmp)
        else:
            heapq.heappush(low, -tmp)
    elif len(low) == 0:
        heapq.heappush(low, -tmp)
    elif len(high) == 0:
        heapq.heappush(low, -tmp)
    if len(low) - len(high) >= 2:
        heapq.heappush(high, -heapq.heappop(low))
    elif len(high) - len(low) >= 2:
        heapq.heappush(low, -heapq.heappop(high))
    if len(low) > len(high):
        print(-low[0])
    elif len(low) == len(high):
        print(-low[0])
    else:
        print(high[0])