import sys

input = sys.stdin.readline

n = int(input())

connect = [0] * 500001
pair = {}

for _ in range(n):
    first, second  = map(int, input().split())
    connect[first] = second
    pair[second] = first

def search(left, right, target, list):
    while left <= right:
        middle = (left + right) // 2
        if list[middle] < target:
            left = middle + 1
        elif list[middle] > target:
            if list[middle-1] < target:
                return middle
            right = middle - 1
    return middle

dp = [1e9] * (500001)
dp[0] = 0
dp_list = [[] for _ in range(500001)]

for i in range(len(connect)):
    if connect[i] > 0:
        insert = search(0, len(dp), connect[i], dp)
        if dp[insert] == 1e9:
            for j in dp_list[insert-1]:
                dp_list[insert].append(j)
            dp_list[insert].append(connect[i])
        else:
            dp_list[insert] = []
            for j in dp_list[insert-1]:
                dp_list[insert].append(j)
            dp_list[insert].append(connect[i])
        dp[insert] = connect[i]
        
for i in range(len(dp)):
    if dp[i] == 1e9:
        max_count = i-1
        break

res_list = dp_list[max_count]
remove_cnt = len(pair) - max_count
remove_list = []

for i in range(len(connect)):
    if connect[i] == 0 or connect[i] == 1e9:
        continue
    else:
        if not (connect[i] in res_list):
            remove_list.append(pair[connect[i]])
remove_list.sort()
print(remove_cnt)
for i in remove_list:
    print(i)