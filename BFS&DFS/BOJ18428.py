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

    for i in range(4):
        nx = x
        ny = y
        for j in range(len(map)):
            nx += dx[i]
            ny += dy[i]
            if 0 <= nx < len(map) and 0 <= ny < len(map):
                if map[ny][nx] == 'O':
                    break
                elif map[ny][nx] == 'S':
                    return False
    return True

for i in range(n):
    for j in range(n):
        if map[i][j] == 'X':
            empty.append([i, j])
        elif map[i][j] == 'T':
            teacher.append([i, j])
block = list(combinations(empty, 3))

for i in block:
    tmp = copy.deepcopy(map)
    possible = True
    for wy, wx in i:
        tmp[wy][wx] = 'O'
    for ty, tx in teacher:
        if not check(tmp, ty, tx):
            possible = False
            break
    if possible:
        break
if possible:
    print("YES")
else:
    print("NO")







