import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def remove_pin(n, move):
    res = (n, move)
    for i in range(5):
        for j in range(9):
            if world[i][j] == 1:
                for k in range(4):
                    nx = j + dx[k]
                    ny = i + dy[k]
                    if 0 <= nx < 9 and 0 <= ny < 5:
                        if world[ny][nx] == 1:
                            if 0 <= nx + dx[k] < 9 and 0 <= ny + dy[k] < 5:
                                if world[ny+dy[k]][nx+dx[k]] == 0:
                                    world[ny][nx] = 0
                                    world[i][j] = 0
                                    world[ny+dy[k]][nx+dx[k]] = 1
                                    res = min(res, remove_pin(n-1, move+1))
                                    world[ny+dy[k]][nx+dx[k]] = 0
                                    world[i][j] = 1
                                    world[ny][nx] = 1
    return res


n = int(input())

for t in range(n):
    world = [[] for _ in range(5)]
    num_pin = 0
    for i in range(5):
        tmp = input().rstrip()
        for j in tmp:
            if j == '#':
                world[i].append(-1)
            elif j == '.':
                world[i].append(0)
            elif j == 'o':
                world[i].append(1)
                num_pin += 1
    if t != n-1:
        trash = input()
    res = remove_pin(num_pin, 0)
    print(res[0], res[1])