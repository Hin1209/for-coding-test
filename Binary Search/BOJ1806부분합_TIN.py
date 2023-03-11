import sys
from bisect import bisect_left

input = sys.stdin.readline

n, s = map(int, input().split())

num_list = [0] + list(map(int, input().split()))
sum_list = [0]
sum = 0

for i in range(1,len(num_list)):
    sum += num_list[i]
    sum_list.append(sum)

min_length = 1e9

for i in range(1,len(num_list)):
    if sum_list[i] >= s:
        flag = bisect_left(sum_list, sum_list[i] - s)
        if sum_list[i] - sum_list[flag] == s:
            tmp_length = i - flag
        else:
            tmp_length = i - flag + 1
        if min_length > tmp_length:
            min_length = tmp_length

if min_length == 1e9:
    print(0)
else:
    print(min_length)
