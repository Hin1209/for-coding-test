import sys

input = sys.stdin.readline
INF = int(1e9)

t = int(input())

for _ in range(t):
    k = int(input())
    dp = [[INF] * k for _ in range(k)]
    num_list = list(map(int, input().split()))
    sum_list = [num_list[0]]
    for i in range(1,k):
        sum_list.append(sum_list[i-1] + num_list[i])
    for i in range(k):
        dp[i][i] = num_list[i]
    for z in range(k):
        for i in range(k):
            if z == 0:
                dp[i][i] = num_list[i]
            elif z == 1:
                if i+1 == k: continue
                dp[i][i+1] = num_list[i] + num_list[i+1]
            else:
                if i+z >= k: continue
                for j in range(z):
                    if j == 0:
                        compare = num_list[i] +  dp[i+1][i+z] + sum_list[i+z] - sum_list[i]
                    elif j+1 == z:
                        if i == 0:
                            compare = dp[i][i+j] + sum_list[i+j] + num_list[i+z] 
                        else:
                            compare =  dp[i][i+j] + sum_list[i+j] - sum_list[i-1] + num_list[i+z] 
                    else:
                        if i == 0:
                            compare = dp[i][i+j] + dp[i+j+1][i+z] + sum_list[i+z]
                        else:
                            compare = dp[i][i+j] + dp[i+j+1][i+z] + sum_list[i+z] - sum_list[i-1] 
                    dp[i][i+z] = min(dp[i][i+z], compare)
    print(dp[0][k-1])