import sys
from bisect import bisect_left
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
line = []
dp = []

for _ in range(n):
    tmp = int(input())
    line.append(tmp)
    
dp.append(line[0])
for i in range(1, n):
    if line[i] > dp[-1]:
        dp.append(line[i])
    elif line[i] < dp[-1]:
        insert = bisect_left(dp, line[i])
        dp[insert] = line[i]

print(n - len(dp))