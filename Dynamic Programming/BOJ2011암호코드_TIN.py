import sys
from collections import deque 
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

crypt = input().rstrip()

dp = [0] * (len(crypt))

dp[0] = 1
if crypt[0] == '0':
    print('0')
else:
    for i in range(1,len(crypt)):
        if crypt[i] == '0':
            inspect = int(crypt[i-1] + crypt[i])
            if 0 < inspect <= 26:
                dp[i] = (dp[i] + dp[i-2]) % 1000000 if i >= 2 else dp[i] + 1
                dp[i-1] = 0
                continue
            else:
                dp[len(crypt)-1] = 0
                break
        if int(crypt[i-1] + crypt[i]) <= 26:
            dp[i] = (dp[i] + dp[i-2]) % 1000000 if i >= 2 else dp[i] + 1
        dp[i] = (dp[i] + dp[i-1]) % 1000000

    print(dp[len(crypt)-1])