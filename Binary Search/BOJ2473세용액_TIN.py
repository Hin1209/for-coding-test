import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

n = int(input())

num = list(map(int, input().split()))
num.sort()

min_sum = 1e11

for i in range(n-1):
    for j in range(i+1,n-1):
        left = i
        right = j
        sum = num[left] + num[right]
        target = -sum
        flag1 = bisect_left(num, target)
        flag1 = flag1 if flag1 < n else flag1 - 1
        if flag1 <= j:
            flag1 = j+1
        flag2 = flag1 - 1
        if flag2 == j:
            flag2 = flag1
        sum1 = sum + num[flag1]
        sum2 = sum + num[flag2]
        if abs(sum1) <= abs(sum2) and abs(sum1) < min_sum:
            min_sum = abs(sum1)
            optimal_pair = (num[left], num[right], num[flag1])
        elif abs(sum1) > abs(sum2) and abs(sum2) < min_sum:
            min_sum = abs(sum2)
            optimal_pair = (num[left], num[right], num[flag2])

print("{} {} {}".format(optimal_pair[0], optimal_pair[1], optimal_pair[2]))