import sys
from collections import deque
import heapq
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

st1 = input()[:-1]
st2 = input()[:-1]

table = [[0 for _ in range(len(st1)+1)] for _ in range(len(st2)+1)]

for i in range(len(st2)):
    for j in range(len(st1)):
        if st2[i] == st1[j]:
            table[i+1][j+1] = table[i][j] + 1
        else:
            table[i+1][j+1] = max(table[i][j+1], table[i+1][j])
            
res = 0
for i in range(len(table)):
    tmp = max(table[i])
    if tmp > res:
        res = tmp
        
print(res)