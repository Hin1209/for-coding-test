import sys

input = sys.stdin.readline

n = int(input())
cost = []
dp_table = [[0, 0, 0] for _ in range(n)]

for i in range(n):
    cost.append(list(map(int, input().split())))

dp_table[0] = cost[0]

for i in range(1, n):
    for j in range(3):
        dp_table[i][j] = cost[i][j] + min(dp_table[i-1][(j+1)%3], dp_table[i-1][(j-1)%3])

print(min(dp_table[n-1]))




