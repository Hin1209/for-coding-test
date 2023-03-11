import sys

input = sys.stdin.readline

n = int(input())
MOD = 1000000000
check = 1 << 10
dp = [[[0] * check for _ in range(10)] for _ in range(n+1)]
for i in range(1,10):
    dp[1][i][1<<i] = 1
for i in range(2, n+1):
    for j in range(10):
        for k in range(check):
            next = k | (1 << j)
            if j == 0:
                dp[i][j][next] = (dp[i][j][next] + dp[i-1][j+1][k]) 
            elif j == 9:
                dp[i][j][next] = (dp[i][j][next] + dp[i-1][j-1][k]) 
            else:
                dp[i][j][next] = (dp[i][j][next] + dp[i-1][j-1][k]) 
                dp[i][j][next] = (dp[i][j][next] + dp[i-1][j+1][k]) 

res = 0
for i in range(10):
    res = (res + dp[n][i][1023]) % MOD
print(res)