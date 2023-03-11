import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

dx = [0, 1, -1, 0, 0]
dy = [0, 0, 0, -1, 1]
state = [0, 0, 0, 0, 0, 0]
dice = {"floor": 0, "left": 1, "right": 3, "up": 2, "down": 4, "op": 5}
floor = 0

def move(command):
    if command == 1:
        tmp = dice["floor"]
        dice["floor"] = dice["right"]
        dice["right"] = dice["op"]
        dice["op"] = dice["left"]
        dice["left"] = tmp
    elif command == 2:
        tmp = dice["floor"]
        dice["floor"] = dice["left"]
        dice["left"] = dice["op"]
        dice["op"] = dice["right"]
        dice["right"] = tmp
    elif command == 3:
        tmp = dice["floor"]
        dice["floor"] = dice["up"]
        dice["up"] = dice["op"]
        dice["op"] = dice["down"]
        dice["down"] = tmp
    elif command == 4:
        tmp = dice["floor"]
        dice["floor"] = dice["down"]
        dice["down"] = dice["op"]
        dice["op"] = dice["up"]
        dice["up"] = tmp

n, m, y, x, k = map(int, input().split())

world = [[0] * m for _ in range(n)]

for i in range(n):
    scores = list(map(int, input().split()))
    for j in range(m):
        world[i][j] = scores[j]
        
commands = list(map(int, input().split()))

for i in range(k):
    command = commands[i]
    nx = x + dx[command]
    ny = y + dy[command]
    if 0 <= nx < m and 0 <= ny < n:
        move(command)
        if world[ny][nx] == 0:
            world[ny][nx] = state[dice["floor"]]
        else:
            state[dice["floor"]] = world[ny][nx]
            world[ny][nx] = 0
        print(state[dice["op"]])
        x = nx
        y = ny