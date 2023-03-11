import sys

input = sys.stdin.readline

n = int(input())
weight = list(map(int, input().split()))

m = int(input())
check = list(map(int, input().split()))

dp = [[0] * (n+1) for _ in range(40001)]

def solve(total_weight, pos): 
    if total_weight > 40000: return
    if dp[total_weight][pos] == 0:
        dp[total_weight][pos] = 1
    else:
        return
    if pos == n: return
    solve(total_weight+weight[pos], pos+1)
    solve(total_weight, pos+1)
    solve(abs(total_weight-weight[pos]), pos+1)
    
solve(0, 0)
for i in check:
    if 1 in dp[i]:
        print("Y", end=" ")
    else:
        print("N", end=" ")