from collections import deque

def check_turn(robot, board):
    y1, x1 = robot[0]
    y2, x2 = robot[1]
    if robot[2] == 0:
        if y1 > 0:
            if board[y1-1][x1] == 0 and board[y2-1][x2] == 0:
                if x2 > x1:
                    return [[y1-1,x2], [y2, x2], 1, robot[3]+1]
                else:
                    return [[y1-1, x1], [y2, x1], 1, robot[3]+1]
            else:
                return False
        if y1 < len(board)-1:
            if board[y1+1][x1] == 0 and board[y2+1][x2] == 0:
                if x2 > x1:
                    return [[y1+1, x2], [y2, x2], 1, robot[3]+1]
                else:
                    return [[y1+1, x1], [y2, x1], 1, robot[3]+1]
            else:
                return False
    else:
        if x1 > 0:
            if board[y1][x1-1] == 0 and board[y2][x2-1] == 0:
                if y2 > y1:
                    return [[y2, x1-1], [y2, x2], 0, robot[3]+1]
                else:
                    return [[y1, x1], [y1, x2-1], 0, robot[3]+1]
            else:
                return False
        if x1 < len(board)-1:
            if board[y1][x1+1] == 0 and board[y2][x2+1] == 0:
                if y2 > y1:
                    return [[y2, x1+1], [y2, x2], 0, robot[3]+1]
                else:
                    return [[y1, x1], [y1, x2+1], 0, robot[3]+1]

def solution(board):
    answer = 0
    dx = [1, 0]
    dy = [0, 1]
    robot = [[0, 0], [0, 1], 0, 0]
    q = deque()
    q.append(robot)
    stop = 0
    while q:
        tmp = q.popleft()
        for i in range(1, 3):
            if i % 2 == 0:
                if check_turn(tmp, board):
                    robot = check_turn(tmp, board)
                    q.append(robot)
                    answer = robot[3]
                    if robot[0][0] == len(board)-1 and robot[0][1] == len(board)-1:
                        stop = 1
                        break
                    elif robot[1][0] == len(board)-1 and robot[1][1] == len(board)-1:
                        stop = 1
                        break
            else:
                for j in range(2):
                    nx1 = tmp[0][1] + dx[i]
                    ny1 = tmp[0][0] + dy[i]
                    nx2 = tmp[1][1] + dx[i]
                    ny2 = tmp[1][0] + dy[i]
                    if 0 <= nx1 < len(board) and 0 <= ny1 < len(board) and 0 <= nx2 < len(board) and 0 <= ny2 < len(board):
                        robot = [[ny1, nx1], [ny2, nx2], tmp[2], tmp[3]+1]
                        answer = robot[3]
                        if robot[0][0] == len(board) - 1 and robot[0][1] == len(board) - 1:
                            stop = 1
                            break
                        elif robot[1][0] == len(board) - 1 and robot[1][1] == len(board) - 1:
                            stop = 1
                            break
        if stop == 1:
            break
    return answer
print(solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]))