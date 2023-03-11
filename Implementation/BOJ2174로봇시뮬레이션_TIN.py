import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

A, B = map(int, input().split())
N, M = map(int, input().split())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
world = [[0] * (A+1) for _ in range(B+1)]
robots = [0]
for i in range(N):
    x, y, dir = input().rstrip().split()    
    if dir == 'E':
        state = 0
    elif dir == 'N':
        state = 1
    elif dir == 'W':
        state = 2
    elif dir == 'S':
        state = 3
    robots.append([int(y), int(x), state])
    world[int(y)][int(x)] = i+1
    
exit = False
for i in range(M):
    target, command, loop = input().rstrip().split()
    target = int(target)
    loop = int(loop)
    for j in range(loop):
        y, x, s = robots[target]
        if command == 'F':
            ny, nx = y + dy[s], x + dx[s]
            if ny > B or nx > A or ny < 1 or nx < 1:
                print(f"Robot {target} crashes into the wall")
                exit = True
                break
            if world[ny][nx] != 0:
                print(f"Robot {target} crashes into robot {world[ny][nx]}")
                exit = True
                break
            world[y][x] = 0
            world[ny][nx] = target
            robots[target] = [ny, nx, s]
        elif command == 'R':
            robots[target][2] = (robots[target][2] - 1) % 4
        elif command == 'L':
            robots[target][2] = (robots[target][2] + 1) % 4
    if exit:
        break
if not exit:
    print("OK")