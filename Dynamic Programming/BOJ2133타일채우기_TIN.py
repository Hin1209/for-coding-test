import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())

dp = [0] * (n+1)
dp[0] = 1

for i in range(2,n+1):
    dp[i] += 3*dp[i-2]
    back = i-4
    while back >= 0:
        dp[i] += 2*dp[back]
        back -= 2

print(dp[n])