import sys
from collections import deque

input = sys.stdin.readline

size = int(input())
num = list(map(int, input().split()))
n_question = int(input())
possible = [[0] * size for _ in range(size)]
for i in range(size):
    possible[i][i] = 1

for i in range(size):
    flag1 = i-1
    flag2 = i+1
    while 0 <= flag1 and flag2 < size:
        if num[flag1] == num[flag2]:
            possible[flag1][flag2] = 1
            flag1 -= 1
            flag2 += 1
        else:
            break
        
for i in range(size-1):
    flag1 = i
    flag2 = i+1
    while 0 <= flag1 and flag2 < size:
        if num[flag1] == num[flag2]:
            possible[flag1][flag2] = 1
            flag1 -= 1
            flag2 += 1
        else:
            break
                
for _ in range(n_question):
    s, e = map(int, input().split())
    print(possible[s-1][e-1])
    