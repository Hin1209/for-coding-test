from collections import deque
def turn(dr): # 회전 함수
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
snake = deque() # 뱀이 차지하는 좌표를 저장
snake_head = [1, 1] # 뱀의 머리
direction = [0, 1, 2, 3] # 0:북쪽 1:동쪽 2:남쪽 3:서쪽
dirc_sn = 1 # 뱀의 머리가 향하는 방향
time = 0 # 시간
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
snake.append(snake_head) # 뱀의 위치 정보에 머리 위치 저장
for _ in range(apple):
    y, x = list(map(int, input().split()))
    board[y][x] = 1 # 맵 불러오기
change_dirc = int(input())
move = [] # 뱀의 회전 정보 저장
for _ in range(change_dirc):
    line = tuple(input().split())
    move.append(line)
mv_cnt = 0 # 뱀이 회전한 횟수
board[snake_head[0]][snake_head[1]] = 5 # 뱀이 있는 위치는 5로 설정
while True:
    # 뱀이 회전하기 전까지는 그대로 진행, 또는 회전을 모두 끝내면 방향을 더이상 바꾸지 않음
    if time < int(move[mv_cnt][0]) or time > int(move[mv_cnt][0]):
        time += 1
        ny = snake_head[0] + dy[dirc_sn]
        nx = snake_head[1] + dx[dirc_sn]
        if(nx < 1 or nx > n or ny < 1 or ny > n or board[ny][nx] == 5): # 몸이랑 부딪히거나 맵 경계에 닿는 경우 종료
            break
        for y, x in snake: # 원래 있던 자리를 0으로 초기화
            board[y][x] = 0
        if(board[ny][nx] == 1): # 사과를 먹는 경우 꼬리는 그대로 두고 머리 부분만 추가함
            board[ny][nx] = 0
            snake_head[0] = ny
            snake_head[1] = nx
            snake.append([snake_head[0], snake_head[1]])
        else: # 사과를 먹지 않는 경우 꼬리를 지우고 머리가 한 칸 앞으로 감
            snake.popleft()
            snake_head[0] = ny
            snake_head[1] = nx
            snake.append([snake_head[0], snake_head[1]])
        for y, x in snake:
            board[y][x] = 5 # 뱀이 위치하는 부분 다시 5로 설정
    elif time == int(move[mv_cnt][0]): # 회전을 할 시간이 되면 회전 시키고 움직임
        turn(move[mv_cnt][1])
        if mv_cnt < len(move) - 1: # 회전 횟수를 증가시키는데 mv_cnt가 len(move)를 넘지 않게끔 설정
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