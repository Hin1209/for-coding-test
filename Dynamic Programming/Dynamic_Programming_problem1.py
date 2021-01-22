test_case = int(input())
for _ in range(test_case):
    n, m = list(map(int, input().split()))
    tmp_data = list(map(int, input().split()))
    # 데이터를 추가하기 위해 거꾸로 정렬(pop)이 가장 뒤에 있는 원소부터 빼냄
    tmp_data.reverse()
    mine = [[] for _ in range(n)]
    dp_table = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            mine[i].append(tmp_data.pop())
    for i in range(n):
        dp_table[i][0] = mine[i][0]
    # 이동 방향이 왼쪽에서 오른쪽, x 축 방향이므로, x 좌표를 먼저 고정시키고 y축을 검사 한 후 x 좌표를 이동시켜야 함
    for j in range(1, m):
        for i in range(n):
            # 맨 위로 오는 경우
            if i == 0:
                dp_table[i][j] = mine[i][j] + max(dp_table[i][j-1], dp_table[i+1][j-1])
            # 맨 아래로 오는 경우
            elif i == n-1:
                dp_table[i][j] = mine[i][j] + max(dp_table[i][j-1], dp_table[i-1][j-1])
            else:
                dp_table[i][j] = mine[i][j] + max(dp_table[i-1][j-1], dp_table[i][j-1], dp_table[i+1][j-1])
    result = 0
    for i in range(n):
        if result < dp_table[i][m-1]:
            result = dp_table[i][m-1]
    print(result)


