import sys
import heapq

input = sys.stdin.readline

N = int(input())

h = []

for _ in range(N):
    operator = int(input())

    if operator > 0:
        heapq.heappush(h, (operator, 1))
    elif operator < 0:
        heapq.heappush(h, (-operator, 0))
    else:
        if not h:
            print(0)
        else:
            num, sign = heapq.heappop(h)
            if sign:
                print(num)
            else:
                print(-num)