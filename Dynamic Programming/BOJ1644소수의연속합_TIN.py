from re import I
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())

isPrime = [True] * (4000001)
isPrime[0] = False; isPrime[1] = False

num_prime = []

for i in range(2, len(isPrime)):
    if isPrime[i]:
        num_prime.append(i)
        j = 2
        while i*j < 4000001:
            isPrime[i*j] = False
            j += 1
            
sum = 0
flag1 = 0
flag2 = 0
cnt = 0
while True:
    if sum >= n:
        sum -= num_prime[flag1]
        flag1 += 1
    elif flag2 == len(num_prime):
        break
    else:
        sum += num_prime[flag2]
        flag2 += 1
    if sum == n:
        cnt += 1
print(cnt)