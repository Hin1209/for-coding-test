import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
tmp = n

m = 0
while tmp > 0:
    m += 1
    tmp //= 10

deq = deque()
deq.append((n, 0))

visited = [-1] * 10000000
visited[n] = 0
res = 0

def check_digit(num, digit):
    for _ in range(digit-1):
        num //= 10
    return num % 10

while deq:
    num, cnt = deq.popleft()
    if cnt == k:
        res = max(res, num)
        continue
    for i in range(1,m):
        for j in range(i+1,m+1):
            num1 = check_digit(num, i)
            num2 = check_digit(num, j)
            if j == m and num1 == 0: continue
            tmp = num
            tmp -= num1 * (10**(i-1))
            tmp -= num2 * (10**(j-1))
            tmp += num2 * (10**(i-1))
            tmp += num1 * (10**(j-1))
            if visited[tmp] < cnt+1:
                visited[tmp] = cnt+1
                deq.append((tmp, cnt+1))
print(res) if res > 0 else print(-1)