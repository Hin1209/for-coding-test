import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m = map(int, input().split())

num = []
for _ in range(n):
    tmp = int(input())
    num.append(tmp)
    
min_tree = [0] * (4 * n)
max_tree = [0] * (4 * n)
def init_min_tree(start, end, node):
    if start == end:
        min_tree[node] = num[start]
        return min_tree[node]
    mid = (start + end) // 2
    min_tree[node] = min(init_min_tree(start, mid, 2 * node), init_min_tree(mid+1, end, 2 * node + 1))
    return min_tree[node]

def find_min(start, end, node, left, right):
    if left > end or right < start:
        return 1e10
    if left <= start and end <= right:
        return min_tree[node]
    mid = (start + end) // 2
    return min(find_min(start, mid, 2 * node, left, right), find_min(mid+1, end, 2 * node + 1, left, right))

def init_max_tree(start, end, node):
    if start == end:
        max_tree[node] = num[start]
        return max_tree[node]
    mid = (start + end) // 2
    max_tree[node] = max(init_max_tree(start, mid, 2 * node), init_max_tree(mid+1, end, 2 * node + 1))
    return max_tree[node]

def find_max(start, end, node, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return max_tree[node]
    mid = (start + end) // 2
    return max(find_max(start, mid, 2 * node, left, right), find_max(mid+1, end, 2 * node + 1, left, right))
init_min_tree(0, n-1, 1)
init_max_tree(0, n-1, 1)
res = []
for _ in range(m):
    a, b = map(int, input().split())
    res.append((find_min(0, n-1, 1, a-1, b-1), find_max(0, n-1, 1, a-1, b-1)))
for small, big in res:
    print(small, big)