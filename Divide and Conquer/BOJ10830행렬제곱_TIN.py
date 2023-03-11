import sys
sys.setrecursionlimit(10**7)

input = sys.stdin.readline

n, b = map(int, input().split())

mat = []
for _ in range(n):
    mat.append(list(map(int, input().split())))

def matmul(a, b):
    res = [[0] * len(a) for _ in range(len(b[0]))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            sum = 0
            for k in range(len(a[0])):
                sum += a[i][k] * b[k][j] % 1000
            res[i][j] = sum % 1000
    return res
    
def matpow(a, b):
    if b == 1:
        return a
    if b % 2 == 0:
        tmp = matpow(a, b//2)
        return matmul(tmp, tmp)
    else:
        tmp = matpow(a, b//2)
        tmp = matmul(tmp, tmp)
        return matmul(a, tmp)
res = matpow(mat, b)
for i in range(len(res)):
    for j in range(len(res[0])):
        print(res[i][j] % 1000, end=" ")
    print()