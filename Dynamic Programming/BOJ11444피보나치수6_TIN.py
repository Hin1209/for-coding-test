import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
memo = dict()
mod = 1000000007

def solve(num):
    if not num in memo.keys():    
        if num == 0:
            memo[num] = 0
        elif num == 1:
            memo[num] = 1
        elif num % 2 == 0:
            even = solve(num//2)
            odd = solve(num//2-1)
            memo[num] = even * (even + 2 * odd) % mod
        else:
            even = solve(num//2 + 1)
            odd = solve(num//2)
            memo[num] = (even ** 2 + odd ** 2) % mod
    return memo[num]
        
print(solve(n))
