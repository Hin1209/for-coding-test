test_case = int(input())
for _ in range(test_case):
    n, m = list(map(int, input().split()))
    tmp_data = list(map(int, input().split()))
    tmp_data.reverse()
    mine = [[] for _ in range(n)]
    dp_table = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            mine[i].append(tmp_data.pop())
    for i in range(n):
        dp_table[i][0] = mine[i][0]
    for j in range(1, m):
        for i in range(n):
            if i == 0:
                dp_table[i][j] = mine[i][j] + max(dp_table[i][j-1], dp_table[i+1][j-1])
            elif i == n-1:
                dp_table[i][j] = mine[i][j] + max(dp_table[i][j-1], dp_table[i-1][j-1])
            else:
                dp_table[i][j] = mine[i][j] + max(dp_table[i-1][j-1], dp_table[i][j-1], dp_table[i+1][j-1])
    result = 0
    for i in range(n):
        if result < dp_table[i][m-1]:
            result = dp_table[i][m-1]
    print(result)


