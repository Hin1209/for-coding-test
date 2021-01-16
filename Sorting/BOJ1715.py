import sys
import heapq
from collections import deque
n = int(sys.stdin.readline())
card = []
deck = deque()
result = 0
for i in range(n):
    heapq.heappush(card, int(sys.stdin.readline()))
while len(card) != 1:
    left = heapq.heappop(card)
    right = heapq.heappop(card)
    result += left + right
    heapq.heappush(card, left+right)

print(result)
