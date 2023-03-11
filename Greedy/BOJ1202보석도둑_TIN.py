import sys
import heapq

input = sys.stdin.readline

n, k = map(int, input().split())
diamond = []

for _ in range(n):
    weight, value = map(int, input().split())
    diamond.append((weight, value))
diamond.sort()

bag = []
for _ in range(k):
    bag.append(int(input()))
bag.sort()

sum_values = 0
h = []
j = 0
for i in bag:
    while j < len(diamond) and diamond[j][0] <= i:
        heapq.heappush(h, -diamond[j][1])
        j += 1
    if h:
        sum_values -= heapq.heappop(h)
print(sum_values)    