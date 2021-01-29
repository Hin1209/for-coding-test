from itertools import combinations
import copy
n = int(input())
map = []
for i in range(n):
    map.append(list(input().split()))
empty = []
teacher = []
possible = True

def check(map, y, x):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    # 상하좌우 검사
    for i in range(4):
        nx = x
        ny = y
        # 상하좌우 방향의 맵 끝까지 검사해야함
        for j in range(len(map)):
            nx += dx[i]
            ny += dy[i]
            # 맵 안의 인덱스만 검사
            if 0 <= nx < len(map) and 0 <= ny < len(map):
                # 벽을 만나면 다른 방향 검사함
                if map[ny][nx] == 'O':
                    break
                # 학생을 만나면 False 반환
                elif map[ny][nx] == 'S':
                    return False
    # 모든 방향을 검사했을때 학생을 만나는 경우가 없으면 True 반환
    return True

for i in range(n):
    for j in range(n):
        if map[i][j] == 'X':
            empty.append([i, j])
        elif map[i][j] == 'T':
            teacher.append([i, j])
# 벽을 세울 수 있는 모든 경우의 수를 저장
block = list(combinations(empty, 3))

for i in block:
    # 매번 맵을 카피해 새로 검사함
    tmp = copy.deepcopy(map)
    possible = True
    # 벽을 세움
    for wy, wx in i:
        tmp[wy][wx] = 'O'
    # 모든 선생님의 위치에 대해 check 함수 실행
    for ty, tx in teacher:
        if not check(tmp, ty, tx):
            # 학생이 발견되는 경우가 있으면 possible을 False로 설정
            possible = False
            break
    # 학생이 발견되지 않는 경우가 하나라도 있으면 반복문 종료
    if possible:
        break

if possible:
    print("YES")
else:
    print("NO")







