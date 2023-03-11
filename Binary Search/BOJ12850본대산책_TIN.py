from audioop import mul
import sys

input = sys.stdin.readline
graph = [[0,1,1,0,0,0,0,0],
         [1,0,1,1,0,0,0,0],
         [1,1,0,1,1,0,0,0],
         [0,1,1,0,1,1,0,0],
         [0,0,1,1,0,1,0,1],
         [0,0,0,1,1,0,1,0],
         [0,0,0,0,0,1,0,1],
         [0,0,0,0,1,0,1,0]]
mod = 1000000007
d = int(input())

def multiply(a, b):
    res = [[0] * 8 for _ in range(8)]
    for i in range(8):
        for j in range(8):
            for k in range(8):
                res[i][j] += a[i][k] * b[k][j] % mod
                res[i][j] %= mod
    return res

def pow(a, p):
    if p == 1:
        return a
    if p % 2 == 1:
        tmp = pow(a, p-1)
        return multiply(a, tmp)
    else:
        tmp = pow(a, p//2)
        return multiply(tmp, tmp)

answer = pow(graph, d)
print(answer[0][0])   

 