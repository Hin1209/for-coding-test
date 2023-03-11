import sys

input = sys.stdin.readline

target = list(map(int, input().split()))

def move(start, end):
    if start == end:
        return 1
    if start == 0:
        return 2
    if abs(start - end) == 2:
        return 4
    if abs(start - end) == 1 or abs(start - end) == 3:
        return 3
    
INF = 1e9
dp = [[[INF] * 5 for _ in range(5)] for _ in range(len(target))]
dp[0][0][0] = 0
for i in range(len(target)):
    if target[i] == 0:
        break
    for j in range(5):
        for k in range(5):
            if dp[i][j][k] != INF:
                move_left = move(j, target[i])
                move_right = move(k, target[i])
                if dp[i+1][target[i]][k] > dp[i][j][k] + move_left:
                    dp[i+1][target[i]][k] = dp[i][j][k] + move_left
                if dp[i+1][j][target[i]] > dp[i][j][k] + move_right:
                    dp[i+1][j][target[i]] = dp[i][j][k] + move_right
    
res = INF
for i in range(5):
    for j in range(5):
        if dp[len(target)-1][i][j] < res:
            res = dp[len(target)-1][i][j]
print(res)