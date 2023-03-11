import sys
from collections import deque
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

given, target = map(int, input().split())

deq = deque()

deq.append((given, 1))

res = -1

while deq:
    num, cnt = deq.popleft()
    if num == target:
        res = cnt
        break
    if num > target:
        continue
    num_double = 2*num
    push_one = 10*num + 1
    deq.append((num_double,cnt+1))
    deq.append((push_one,cnt+1))
    
print(res)