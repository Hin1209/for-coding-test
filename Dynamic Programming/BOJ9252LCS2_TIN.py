import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()

table = [[0] * (len(str1) + 1) for _ in range(len(str2) + 1)]

max_length = 0

for i in range(1, len(str2) + 1):
    for j in range(1, len(str1) + 1):
        if str2[i-1] == str1[j-1]:
            table[i][j] = table[i-1][j-1] + 1
            if table[i][j] > max_length:
                max_length = table[i][j]
                max_pair = (i, j)
        else:
            table[i][j] = max(table[i-1][j],table[i][j-1])
            if table[i][j] > max_length:
                max_length = table[i][j]
                max_pair = (i, j)
                
def print_str(str1, str2, i, j):
    if table[i][j] == 0: return
    if str1[j-1] == str2[i-1]:
        print_str(str1, str2, i-1, j-1)
        print(str1[j-1], end="")
    else:
        if table[i-1][j] > table[i][j-1]:
            print_str(str1, str2, i-1, j)
        else:
            print_str(str1, str2, i, j-1)

if max_length == 0:
    print(0)
else:
    print(max_length)
    print_str(str1, str2, max_pair[0], max_pair[1])