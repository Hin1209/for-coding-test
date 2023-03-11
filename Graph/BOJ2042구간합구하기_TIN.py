import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m, k = map(int, input().split())

n_list = []
for _ in range(n):
    tmp = int(input())
    n_list.append(tmp)
    
tree = [0] * (4*n)

def init_tree(start, end, node):
    if start == end:
        tree[node] = n_list[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = init_tree(start, mid, node * 2) + init_tree(mid+1, end, node * 2 + 1)
    return tree[node]

def sum(start, end, node, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return sum(start, mid, node * 2, left, right) + sum(mid+1, end, node * 2 + 1, left, right)


def update(start, end, node, index, diff):
    if index < start or index > end:
        return
    tree[node] += diff
    if start == end: 
        return
    mid = (start + end) // 2
    update(start, mid, node*2, index, diff)
    update(mid+1, end, node*2+1, index, diff)

init_tree(0, n-1, 1)
res = []
for _ in range(m+k):
    case, a, b = map(int, input().split())
    if case == 1:
        dif = b - n_list[a-1]
        n_list[a-1] = b
        update(0, n-1, 1, a-1, dif)
    else:
        res.append(sum(0, n-1, 1, a-1, b-1))

for i in res:
    print(i)
    
