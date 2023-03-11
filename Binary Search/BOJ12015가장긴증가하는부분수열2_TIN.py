import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())

num_list = list(map(int, input().split()))

dp = [1e9]
for i in range(len(num_list)):
    if dp[-1] < num_list[i]:
        dp.append(num_list[i])
    elif dp[-1] > num_list[i]:
        insert = bisect_left(dp, num_list[i])
        dp[insert] = num_list[i]

print(len(dp))