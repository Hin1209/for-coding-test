import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m, k = map(int, input().split())
mod = 1000000007
nums = []
for _ in range(n):
    tmp = int(input())
    nums.append(tmp)
    
tree = [0] * (4*n)

def init_tree(start, end, node):
    if start == end:
        tree[node] = nums[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = init_tree(start, mid, 2 * node) * init_tree(mid+1, end, 2 * node + 1) % mod
    return tree[node]

def multiply(start, end, node, left, right):
    if left > end or right < start:
        return 1
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return multiply(start, mid, 2 * node, left, right) * multiply(mid+1, end, 2 * node + 1, left, right) % mod

def update(start, end, node, index, change):
    if index < start or end < index:
        return tree[node]
    if start == end:
        if start == index:
            tree[node] = change
            return change
        else:
            return tree[node]
    mid = (start + end) // 2
    tree[node] = update(start, mid, 2 * node, index, change) * update(mid+1, end, 2 * node + 1, index, change) % mod
    return tree[node]
    
    
init_tree(0, n-1, 1)
res = []
for _ in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        update(0, n-1, 1, b-1, c)
        nums[b-1] = c
    else:
        res.append(multiply(0, n-1, 1, b-1, c-1))
for i in res:
    print(i)