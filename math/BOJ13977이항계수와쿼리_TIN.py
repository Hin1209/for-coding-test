import sys
input = sys.stdin.readline

m = int(input())
res = []
mod = 1000000007

def pow(n, p):
    if p == 0:
        return 1
    if p == 1:
        return n % mod
    if p % 2 == 1:
        return n * pow(n, p - 1) % mod
    tmp = pow(n, p // 2)
    return tmp * tmp % mod

table = [0] * 4000001
inverse = [0] * 4000001
inverse[0] = 1
table[0] = 1
for i in range(1, 4000001):
    table[i] = table[i-1] * i % mod
    
for _ in range(m):
    n, k = map(int, input().split())
    print(table[n] * pow(table[k], mod-2) * pow(table[n-k], mod-2) % mod)