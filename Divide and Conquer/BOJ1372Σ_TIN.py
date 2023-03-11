import sys
import heapq

input = sys.stdin.readline

mod = 1000000007

def gcd(a, b):
    while(b):
        a, b = b, int(a%b)
    return a

def pow(n, k):
    if k == 1: return n
    if k % 2 == 1: return n * pow(n, k-1) % mod
    tmp = pow(n, k//2)
    return tmp * tmp % mod

n = int(input())

ans = 0 

for i in range(n):
    d, n = map(int, input().split())
    g = gcd(d, n)
    d //= g
    n //= g
    res = pow(d, mod-2)
    ans += n * res % mod
    ans %= mod

print(ans)