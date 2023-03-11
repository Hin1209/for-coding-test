import sys
from bisect import bisect_left

input = sys.stdin.readline

n = int(input())

num_list = list(map(int, input().split()))
INF = 1e10
dp = [-INF]
max_count = 0
dp_list = []

for i in range(len(num_list)):
    if dp[-1] < num_list[i]:
        dp.append(num_list[i])
        max_count = len(dp) - 1
        dp_list.append((max_count, num_list[i]))
    else:
        insert = bisect_left(dp, num_list[i])
        if dp[insert] == num_list[i]:
            continue
        dp_list.append((insert, num_list[i]))
        dp[insert] = num_list[i]

print(max_count)
res = []
for i in reversed(range(len(dp_list))):
    length, num = dp_list[i]
    if length == max_count:
        res.append(num)
        max_count -= 1
    
for i in range(len(res)):
    print(res.pop(), end=" ")
