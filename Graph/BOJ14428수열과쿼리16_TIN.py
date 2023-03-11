import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

m = int(input())
tree = [0] * (4 * n)

def init_tree(start, end, node):
    if start == end:
        tree[node] = (start, nums[start])
        return tree[node]
    mid = (start + end) // 2
    left = init_tree(start, mid, 2 * node)
    right = init_tree(mid+1, end, 2 * node + 1)
    if left[1] > right[1]:
        tree[node] = (right[0], right[1])
    else:
        tree[node] = (left[0], left[1])
    return tree[node]

def update(start, end, node, index, change):
    if index < start or index > end:
        return tree[node]
    if start == end:
        if start == index:
            tree[node] = (index, change)
            return tree[node]
        else:
            return tree[node]
    mid = (start + end) // 2
    left = update(start, mid, 2 * node, index, change)
    right = update(mid+1, end, 2 * node + 1, index, change)
    if left[1] > right[1]:
        tree[node] = (right[0], right[1])
    else:
        tree[node] = (left[0], left[1])
    return tree[node]

def find_min(start, end, node, left, right):
    if start > right or left > end:
        return (1e9, 1e9+1)
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    l = find_min(start, mid, 2 * node, left, right)
    r = find_min(mid+1, end, 2 * node + 1, left, right)
    if l[1] > r[1]:
        return (r[0], r[1])
    else:
        return (l[0], l[1])
init_tree(0, n-1, 1)
res = []
for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 1:
        nums[b-1] = c
        update(0, n-1, 1, b-1, c)
    else:
        res.append(find_min(0, n-1, 1, b-1, c-1))
for i in res:
    print(i[0] + 1)