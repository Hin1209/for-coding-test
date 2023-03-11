import sys
input = sys.stdin.readline

n = int(input())

dp = [[0] * 53 for _ in range(53)]
dp[0][0] = 1

def find_combination(n, r):
    if dp[n][r] != 0:
        return dp[n][r]
    if n == 0 or r == 0:
        dp[n][r] = 1
        return dp[n][r]
    if n == r:
        dp[n][r] = 1
        return dp[n][r]
    left = find_combination(n-1, r-1)
    right = find_combination(n-1, r)
    dp[n][r] = left + right
    dp[n][r] %= 10007
    return dp[n][r]

for i in range(53):
    for j in range(i+1):
        find_combination(i, j)

if n < 4:
    print(0)
else:
    four = n // 4
    not_four = n - 4 * four
    win = 0
    for i in range(1, four+1):
        if i % 2 == 1:
            win += dp[13][i] * dp[52-i*4][n-i*4]
        else:
            win -= dp[13][i] * dp[52-i*4][n-i*4]
        win %= 10007
    if win < 0:
        win += 10007
    print(win)