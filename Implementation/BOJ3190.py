from collections import deque
def turn(dr):
    global dirc_sn
    if dr == 'L':
        if dirc_sn == 0:
            dirc_sn = 3
        else:
            dirc_sn -= 1
    elif dr == 'D':
        if dirc_sn == 3:
            dirc_sn = 0
        else:
            dirc_sn += 1

n = int(input())
apple = int(input())
board = [[0 for _ in range(n+1)] for _ in range(n+1)]
snake = deque()
snake_head = [1, 1]
direction = [0, 1, 2, 3]
dirc_sn = 1
time = 0
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
snake.append(snake_head)
for _ in range(apple):
    y, x = list(map(int, input().split()))
    board[y][x] = 1
change_dirc = int(input())
move = []
for _ in range(change_dirc):
    line = tuple(input().split())
    move.append(line)
mv_cnt = 0
board[snake_head[0]][snake_head[1]] = 5
while True:
    if time < int(move[mv_cnt][0]) or time > int(move[mv_cnt][0]):
        time += 1
        ny = snake_head[0] + dy[dirc_sn]
        nx = snake_head[1] + dx[dirc_sn]
        if(nx < 1 or nx > n or ny < 1 or ny > n or board[ny][nx] == 5):
            break
        for y, x in snake:
            board[y][x] = 0
        if(board[ny][nx] == 1):
            board[ny][nx] = 0
            snake_head[0] = ny
            snake_head[1] = nx
            snake.append([snake_head[0], snake_head[1]])
        else:
            snake.popleft()
            snake_head[0] = ny
            snake_head[1] = nx
            snake.append([snake_head[0], snake_head[1]])
        for y, x in snake:
            board[y][x] = 5
    elif time == int(move[mv_cnt][0]):
        turn(move[mv_cnt][1])
        if mv_cnt < len(move) - 1:
            mv_cnt += 1
        time += 1
        ny = snake_head[0] + dy[dirc_sn]
        nx = snake_head[1] + dx[dirc_sn]
        if (nx < 1 or nx > n or ny < 1 or ny > n or board[ny][nx] == 5):
            break
        for y, x in snake:
            board[y][x] = 0
        if (board[ny][nx] == 1):
            board[ny][nx] = 0
            snake_head[0] = ny
            snake_head[1] = nx
            snake.append([snake_head[0], snake_head[1]])
        else:
            snake.popleft()
            snake_head[0] = ny
            snake_head[1] = nx
            snake.append([snake_head[0], snake_head[1]])
        for y, x in snake:
            board[y][x] = 5

print(time)