import sys

input = sys.stdin.readline

string = input().rstrip()

dp = [[0] * len(string) for _ in range(len(string))]
for i in range(len(string)):
    dp[i][i] = 1

for i in range(len(string)):
    flag1 = i-1
    flag2 = i+1
    while 0 <= flag1 and flag2 < len(string):
        if string[flag1] == string[flag2]:
            dp[flag1][flag2] = 1
            flag1 -= 1
            flag2 += 1
        else:
            break

for i in range(len(string)):
    flag1 = i
    flag2 = i+1
    while 0 <= flag1 and flag2 < len(string):
        if string[flag1] == string[flag2]:
            dp[flag1][flag2] = 1
            flag1 -= 1
            flag2 += 1
        else:
            break

cnt = 2500 
min_cnt = [0] + [3000] * (len(string))
min_cnt[1] = 1
for i in range(len(string)):
    for j in range(i, len(string)):
        if dp[i][j] != 0:
            min_cnt[j+1] = min(min_cnt[j+1], min_cnt[i] + 1)
print(min_cnt[len(string)])