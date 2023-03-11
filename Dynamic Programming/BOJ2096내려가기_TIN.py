import sys
input = sys.stdin.readline

n = int(input())

INF = 1e9
score = []
pre_max = [0, 0, 0]
pre_min = [0, 0, 0]
max_dp = [0,0,0]
min_dp = [0,0,0]

for i in range(n):
    tmp = list(map(int, input().split()))
    max_dp[0] = max(tmp[0]+pre_max[0], tmp[0]+pre_max[1])
    min_dp[0] = min(tmp[0]+pre_min[0], tmp[0]+pre_min[1])
    max_dp[1] = max(tmp[1]+pre_max[0], tmp[1]+pre_max[1], tmp[1]+pre_max[2])
    min_dp[1] = min(tmp[1]+pre_min[0], tmp[1]+pre_min[1], tmp[1]+pre_min[2])
    max_dp[2] = max(tmp[2]+pre_max[2], tmp[2]+pre_max[1])
    min_dp[2] = min(tmp[2]+pre_min[2], tmp[2]+pre_min[1])
    for j in range(3):
        pre_max[j] = max_dp[j]
        pre_min[j] = min_dp[j]

res_max = max(max_dp)
res_min = min(min_dp)
print(res_max, res_min)