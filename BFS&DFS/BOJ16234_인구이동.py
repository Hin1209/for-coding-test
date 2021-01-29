from collections import deque
import sys
n, l, r = list(map(int, sys.stdin.readline().rstrip().split()))
country = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# 인구가 이동한 횟수
circular = 0

while True:
    if n == 1:
        break
    # 동맹을 나타내기 위한 리스트
    alliance = [[0 for _ in range(n)] for _ in range(n)]
    # 연합 번호
    cnt = 1
    for i in range(n):
        for j in range(n):
            # 동맹이 없을 경우 주변에 동맹을 맺을 수 있는 국가가 있는지 검사
            if alliance[i][j] == 0:
                q = deque()
                q.append([i, j])
                # 동맹 국가의 총 인원
                sum_people = country[i][j]
                # 연합 국가의 수
                union = 1
                # 연합 국가의 좌표
                ally = []
                ally.append([i, j])
                alliance[i][j] = cnt
                while q:
                    y, x = q.popleft()
                    for c in range(4):
                        ny = y + dy[c]
                        nx = x + dx[c]
                        if 0 <= nx < n and 0 <= ny < n:
                            # 동맹을 맺을 수 있는 국가면 동맹에 추가시킴
                            if l <= abs(country[y][x] - country[ny][nx]) <= r and alliance[ny][nx] == 0:
                                alliance[ny][nx] = cnt
                                union += 1
                                sum_people += country[ny][nx]
                                q.append([ny, nx])
                                ally.append([ny, nx])
                # 동맹 국가의 인원을 나눔
                for ay, ax in ally:
                    country[ay][ax] = sum_people // union
                cnt += 1
    # 더 이상 인구 이동이 없는 경우 반복문 종료
    if cnt == n * n + 1:
        break
    circular += 1
print(circular)






# 5 10 20
# 10 15 30 40 15
# 15 30 60 55 20
# 30 20 50 45 40
# 10 15 40 5 10
# 20 5 10 20 15

# 4 10 50
# 10 100 20 90
# 80 100 60 70
# 70 20 30 40
# 50 20 100 10