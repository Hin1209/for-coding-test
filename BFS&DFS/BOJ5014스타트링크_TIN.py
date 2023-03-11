import sys
from collections import deque 
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())

INF = int(1e9)
dp = [INF] * (F+1)
dp[S] = 0

deq = deque()
deq.append((S, 0))

while deq:
    floor, cnt = deq.popleft()
    if floor == G:
        break
    go_down = floor - D
    go_up = floor + U
    if go_down > 0 and dp[go_down] == INF:
        dp[go_down] = cnt + 1
        deq.append((go_down, cnt+1))
    if go_up <= F and dp[go_up] == INF:
        dp[go_up] = cnt + 1
        deq.append((go_up, cnt+1))

if dp[G] == INF:
    print("use the stairs")
else:
    print(dp[G])