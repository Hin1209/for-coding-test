n = int(input())
triangle = []
dp_table = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    triangle.append(tmp)
    dp_table.append([0 for _ in range(len(tmp))])
dp_table[0][0] = triangle[0][0]
for i in range(1, n):
    for j in range(len(triangle[i])):
        if j == 0:
            dp_table[i][j] = triangle[i][j] + dp_table[i-1][j]
        elif j == len(triangle[i]) - 1:
            dp_table[i][j] = triangle[i][j] + dp_table[i-1][j-1]
        else:
            dp_table[i][j] = triangle[i][j] + max(dp_table[i-1][j], dp_table[i-1][j-1])
result = 0
for i in range(len(dp_table[n-1])):
    if result < dp_table[n-1][i]:
        result = dp_table[n-1][i]
print(result)
