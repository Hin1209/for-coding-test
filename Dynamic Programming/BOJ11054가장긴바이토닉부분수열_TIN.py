import sys
import heapq

input = sys.stdin.readline

length = int(input())
num_list = list(map(int, input().split()))

def make_dp(num_list):
    global length
    res = [1] * length
    for i in range(1,length):
        for j in reversed(range(i)):
            if num_list[i] > num_list[j]:
                res[i] = max(res[i], res[j]+1)
    return res

front = make_dp(num_list)
num_list.reverse()
back = (make_dp(num_list))
back.reverse()

count = 0
for i in range(length):
    if count < front[i] + back[i] - 1:
        count = front[i] + back[i] - 1
print(count)