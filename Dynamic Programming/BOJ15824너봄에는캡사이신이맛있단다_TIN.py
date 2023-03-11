import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
mod = 1000000007
num = list(map(int, input().split()))
num.sort()
res = 0
dp = [0] * 3000001
dp[1] = 2
dp[0] = 1
for i in range(2, 300001):
    dp[i] = (dp[i-1] * 2) % mod
for i in range(n):
    if i == 0:
        p = dp[n-1]
        res -= (num[i] % mod) * ((dp[n-1] - 1) % mod)
        res %= mod
        continue
    if i == n-1:
        res += (num[i] % mod) * ((dp[n-1] - 1) % mod)
        res %= mod
        continue
    res += (num[i] % mod) * (dp[i] % mod - dp[n-1-i] % mod) % mod
    res %= mod

print(res) 