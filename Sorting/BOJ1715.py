import sys
import heapq
from collections import deque
n = int(sys.stdin.readline())
card = []
deck = deque()
result = 0
for i in range(n):
    # heap 자료형의 card에 덱들을 크기순으로 저장함.
    heapq.heappush(card, int(sys.stdin.readline()))

# 카드에 남아있는 덱이 하나만 남을때까지 반복
while len(card) != 1:
    # left에는 가장 작은 덱을, right에는 두번째로 작은 덱을 저장함.
    left = heapq.heappop(card)
    right = heapq.heappop(card)
    # 카드를 비교한 횟수를 result에 저장.
    result += left + right
    # card에 합쳐진 덱을 추가함.
    heapq.heappush(card, left+right)

print(result)
