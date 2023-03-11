import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

size, sum = map(int, input().split())

table = []

for i in range(size):
    tmp = list(map(int, input().split()))
    table.append(tmp)
    
sum_table = [[0 for i in range(size)] for i in range(size)]
sum_table[0][0] = table[0][0]
previous_sum = sum_table[0][0]

for i in range(size):
    for j in range(size):
        if i == 0 and j == 0: continue
        if i == 0: 
            sum_table[i][j] = sum_table[i][j-1] + table[i][j]
        elif j == 0: 
            sum_table[i][j] = sum_table[i-1][j] + table[i][j]
        else:
            sum_table[i][j] = sum_table[i-1][j] + sum_table[i][j-1] - sum_table[i-1][j-1] + table[i][j]


for i in range(sum):
    x1, y1, x2, y2 = map(int, input().split())
    x1 -= 1; y1 -= 1; x2 -= 1; y2 -= 1
    if x1 == 0 and y1 == 0:
        print(sum_table[x2][y2])
    elif y1 == 0 and x1 != 0:
        print(sum_table[x2][y2] - sum_table[x1-1][y2])
    elif y1 != 0 and x1 == 0:
        print(sum_table[x2][y2] - sum_table[x2][y1-1])
    else:
        print(sum_table[x2][y2] - sum_table[x1-1][y2] - sum_table[x2][y1-1] + sum_table[x1-1][y1-1])
        