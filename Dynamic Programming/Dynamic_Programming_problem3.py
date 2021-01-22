a = input()
b = input()
# a와 b를 늘여놓은 2차원 배열 생성
dp_table = [[0 for _ in range(len(a) + 1)] for _ in range(len(b) + 1)]
# 가로축에 a를 늘여놓음. 가로세로 각각 첫번쨰 줄은 아무것도 없는 상태로 지정
for i in range(1, len(a) + 1):
    dp_table[0][i] = i
for i in range(1, len(b) + 1):
    dp_table[i][0] = i
for i in range(1, len(b) + 1):
    for j in range(1, len(a) + 1):
        # 문자가 같으면 왼쪽 대각선 위에 있는 수와 같게함(삽입 or 삭제x, 같은 것으로 교환한다 생각하고 횟수는 그대로 둠)
        if b[i-1] == a[j-1]:
            dp_table[i][j] = dp_table[i-1][j-1]
        # 문자가 다르면 현재 비교하는 문자를 고려하기 전에 삽입, 교체, 삭제 중 횟수가 가장 적었던 경우에서 +1을 해줌
        else:
            dp_table[i][j] = 1 + min(dp_table[i-1][j], dp_table[i][j-1], dp_table[i-1][j-1])
print(dp_table[-1][-1])