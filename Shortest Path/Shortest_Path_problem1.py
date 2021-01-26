import sys

input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())
student = [[INF for _ in range(N + 1)] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    # 행은 비교의 주체, 열은 비교 대상. 비교 대상이 더 크면 1, 작으면 -1로 저장한다.
    student[a][b] = 1
    student[b][a] = -1

for i in range(1, N + 1):
    student[i][i] = 0

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            # k가 i보다 크고, j가 k보다 크면 j는 i보다 크다 -> 무한이 아닌 양수로 설정
            if student[i][k] >= 0 and student[k][j] >= 0:
                student[i][j] = min(student[i][j], student[i][k] + student[k][j])
            # k가 i보다 작고, j가 k보다 작으면 j는 i보다 작다 -> 음수로 설정
            elif student[i][k] < 0 and student[k][j] < 0:
                student[i][j] = min(student[i][j], student[i][k] + student[k][j])

cnt = 0

for i in range(1, N + 1):
    # 행 안에 무한이 없으면 순위를 매길 수 있다.
    if not INF in student[i][1:]:
        cnt += 1
print(cnt)