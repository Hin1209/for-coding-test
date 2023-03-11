import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

target = int(input())

len_a = int(input())
a = list(map(int, input().split()))

len_b = int(input())
b = list(map(int, input().split()))

sum_A = [0] 
sum_a = 0
for i in range(len_a):
    sum_a += a[i]
    sum_A.append(sum_a)

sum_B = [0]
sum_b = 0
for i in range(len_b):
    sum_b += b[i]
    sum_B.append(sum_b)

cnt = 0

partial_sum_a = []
partial_sum_b = []

for i in range(len_a):
    for j in range(i+1, len_a+1):
        partial_sum_a.append(sum_A[j] - sum_A[i])
        
for i in range(len_b):
    for j in range(i+1, len_b+1):
        partial_sum_b.append(sum_B[j] - sum_B[i])

partial_sum_a.sort()
partial_sum_b.sort()
for aa in partial_sum_a:
    t = target - aa
    left = bisect_left(partial_sum_b, t)
    right = bisect_right(partial_sum_b, t)
    if left < len(partial_sum_b) and partial_sum_b[left] == t:
        if 0 < right and partial_sum_b[right-1] == t:
            cnt += right - left
        else:
            cnt += 1

print(cnt)