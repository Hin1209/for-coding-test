import sys

input = sys.stdin.readline

def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

def digit(n):
    cnt = 0
    while n != 0:
        cnt += 1
        n //= 10
    return cnt

n = int(input())

num = []
len_num = []
for _ in range(n):
    tmp = int(input())
    num.append(tmp)
    len_num.append(10**digit(tmp))

div = int(input())
for i in range(n):
    len_num[i] %= div
size = 1 << n
dp = [[0] * div for _ in range(size)]

dp[0][0] = 1

for i in range(1 << n):
    for j in range(n):
        if i & (1 << j) == 0:
            next = i | (1 << j)
            for k in range(div):
                addNum = num[j]
                nextDiv = ((k * len_num[j]) % div + addNum) % div
                dp[next][nextDiv] += dp[i][k]
                
numerator = dp[size-1][0]
denominator = 1
for i in range(2, n+1):
    denominator *= i
div = gcd(denominator, numerator)
print("{}/{}".format(numerator//div, denominator//div))