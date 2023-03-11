import sys

input = sys.stdin.readline

num, max_weight = map(int, input().split())

carry = []

for _ in range(num):
    weight, value = map(int, input().split())
    carry.append((weight, value))

carry.sort()

bag = [[0 for _ in range(max_weight+1)] for _ in range(num+1)]

for i in range(1,num+1):
    w, v = carry[i-1]
    for j in range(1,max_weight+1):
        if j < w:
            bag[i][j] = bag[i-1][j]
        else:
            bag[i][j] = max(bag[i-1][j-w]+v, bag[i-1][j])
print(bag[num][max_weight])
