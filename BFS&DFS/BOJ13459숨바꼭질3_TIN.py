import sys
from collections import deque

input = sys.stdin.readline

now, brother = map(int, input().split())

INF = 1e9

dp = [INF] * 100001

deq = deque()
deq.append((now, 0))
dp[now] = 0

while deq:
    pos, time = deq.popleft()
    if pos == brother:
        if dp[brother] > dp[pos]:
            dp[brother] = dp[pos]
            break
    elif pos > brother:
        back = pos-1
        if 0 <= back < len(dp):
            if dp[back] > dp[pos]+1:
                dp[back] = dp[pos]+1
                deq.append((back, time+1))    
    else:
        teleport = 2*pos
        front = pos+1
        back = pos-1
        if teleport < len(dp):
            if dp[teleport] > dp[pos]:
                dp[teleport] = dp[pos]
                deq.append((teleport, time))
        if 0 <= front < len(dp):
            if dp[front] > dp[pos]+1:
                dp[front] = dp[pos]+1
                deq.append((front, time+1))
        if 0 <= back < len(dp):
            if dp[back] > dp[pos]+1:
                dp[back] = dp[pos]+1
                deq.append((back, time+1))
        
print(dp[brother])