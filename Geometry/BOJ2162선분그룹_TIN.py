from audioop import mul
import sys

input = sys.stdin.readline

def ccw(p1, p2, p3):
    res = (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p3[0] - p1[0]) * (p2[1] - p1[1])
    if res > 0:
        return 1
    elif res < 0:
        return -1
    else:
        return 0

def isCross(a,b,c,d):
    abc = ccw(a,b,c)
    abd = ccw(a,b,d)
    cda = ccw(c,d,a)
    cdb = ccw(c,d,b)
    if a[0] == b[0] and b[0] == c[0] and c[0] == d[0]:
        if a[1] > b[1]:
            a[1], b[1] = b[1], a[1]
        if c[1] > d[1]:
            c[1], d[1] = d[1], c[1]
        if a[1] <= d[1] and c[1] <= b[1]:
            return True
        else:
            return False
    else:
        if abc * abd == 0 and cda * cdb == 0:
            if a[0] > b[0]:
                a[0], b[0] = b[0], a[0]
                a[1], b[1] = b[1], a[1]
            if c[0] > d[0]:
                c[0], d[0] = d[0], c[0]
                c[1], d[1] = d[1], c[1]
            if a[0] <= d[0] and c[0] <= b[0]:
                return True
            else:
                return False
        elif abc * abd <= 0 and cda * cdb <= 0:
            return True
        else:
            return False
        
n = int(input())
lines = []
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    p1 = [x1, y1]
    p2 = [x2, y2]
    lines.append([p1, p2])

group = [0] * n
for i in range(n):
    group[i] = i
group_cnt = [0] * n

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    
    if a > b:
        parent[a] = b
    else:
        parent[b] = a
        
for i in range(n-1):
    for j in range(i+1,n):
        l1 = lines[i]
        l2 = lines[j]
        if isCross(l1[0], l1[1], l2[0], l2[1]):
            union_parent(group, i, j)

for i in range(n):
    parent = find_parent(group, i)
    group_cnt[parent] += 1
num_lines = 0
num_group = 0
for i in range(n):
    if group_cnt[i] != 0:
        num_group += 1
        if group_cnt[i] > num_lines:
            num_lines = group_cnt[i]
print(num_group)
print(num_lines)