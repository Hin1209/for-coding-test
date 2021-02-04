import sys

def compress(array, sx, sy, ex, ey):
    result = ''
    cmp = array[sy][sx]
    dont = 0
    size = (ex - sx) // 2
    if ex - sx == 1:
        result += str(cmp)
        return result
    for i in range(sy, ey):
        for j in range(sx, ex):
            if cmp != array[i][j]:
                dont = 1
                break
        if dont:
            break
    if dont:
        result += '('
        for i in range(2):
            for j in range(2):
                result += compress(array, sx + size * j, sy + size * i, sx + size * (j + 1), sy + size * (i + 1))
        result += ')'
    else:
        result += str(cmp)
        return result
    return result

input = sys.stdin.readline

N = int(input())
quad_tree = [[] for _ in range(N)]
for j in range(N):
    tmp = input().rstrip()
    for i in range(N):
        quad_tree[j].append(int(tmp[i]))

print(compress(quad_tree, 0, 0, N, N))


