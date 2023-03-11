import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

deq = deque()
deq.append((n,0,[n]))
INF = 1e9
dp = [INF] * (n+1)
while deq:
    num, cnt, num_list = deq.popleft()
    if num == 1:
        res_cnt, res_list = cnt, num_list
        break
    if num == 0:
        continue
    if num % 3 == 0:
        if cnt + 1 < dp[num // 3]:
            dp[num // 3] = cnt + 1
            tmp = []
            for i in num_list:
                tmp.append(i)
            tmp.append(num//3)
            deq.append((num//3, cnt + 1, tmp))
    if num % 2 == 0:
        if cnt + 1 < dp[num // 2]:
            dp[num // 2] = cnt + 1
            tmp = []
            for i in num_list:
                tmp.append(i)
            tmp.append(num//2)
            deq.append((num//2, cnt + 1, tmp))
    if cnt + 1 < dp[num - 1]:
        tmp = []
        for i in num_list:
            tmp.append(i)
        tmp.append(num - 1)
        deq.append((num - 1, cnt + 1, tmp))

print(res_cnt)
for i in res_list:
    print(i, end = " ")