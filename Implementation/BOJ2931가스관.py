import sys
from collections import deque

input = sys.stdin.readline
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

block_list = ['|', '-', '1', '2', '3', '4', '+']
pipe_direction = {'|' : [0,2], '-': [1,3], '+': [0,1,2,3], '1': [0,3], '2': [2,3], '3': [1,2], '4': [0,1]}
r, c = map(int, input().split())
world = [input().rstrip() for _ in range(r)]
visited = [[0] * c for _ in range(r)]
    
def can_enter(block, direction):
    if block == '|':
        if direction % 2 == 0:
            return True
        else:
            return False
    elif block == '-':
        if direction % 2 == 1:
            return True
        else:
            return False
    elif block == '+':
        return True
    elif block == '1':
        if direction == 0 or direction == 3:
            return True
        else:
            return False
    elif block == '2':
        if direction == 2 or direction == 3:
            return True
        else:
            return False
    elif block == '3':
        if direction == 1 or direction == 2:
            return True
        else:
            return False
    elif block == '4':
        if direction == 0 or direction == 1:
            return True
        else:
            return False
        
def move(block, direction):
    if block == '|':
        if direction == 0:
            return [[-1], [0], [0]]
        else:
            return [[1], [0], [2]]
    elif block == '-':
        if direction == 1:
            return [[0], [1], [1]]
        else:
            return [[0], [-1], [3]]
    elif block == '+':
        return [[-1,0,1,0], [0,1,0,-1], [0,1,2,3]]
    elif block == '1':
        if direction == 0:
            return [[0], [1], [1]]
        else:
            return [[1], [0], [2]]
    elif block == '2':
        if direction == 3:
            return [[-1], [0], [0]]
        else:
            return [[0], [1], [1]]
    elif block == '3':
        if direction == 1:
            return [[-1], [0], [0]]
        else:
            return [[0], [-1], [3]]
    elif block == '4':
        if direction == 1:
            return [[1], [0], [2]]
        else:
            return [[0], [-1], [3]]
            
start = 0
end = 0
for i in range(r):
    for j in range(c):
        if world[i][j] == 'M':
            start = (i, j)
            visited[i][j] = 1
        elif world[i][j] == 'Z':
            end = (i, j)
            visited[i][j] = 1
    
deq = deque()
for i in range(4):
    ny, nx = start[0]+dy[i], start[1]+dx[i]
    if 0 <= ny < r and 0 <= nx < c:
        if world[ny][nx] != '.' and world[ny][nx] != 'Z':
            if can_enter(world[ny][nx], i):
                visited[ny][nx] = 1
                deq.append((ny, nx, i))

for i in range(4):
    ny, nx = end[0]+dy[i], end[1]+dx[i]
    if 0 <= ny < r and 0 <= nx < c:
        if world[ny][nx] != '.' and world[ny][nx] != 'M':
            if can_enter(world[ny][nx], i):
                visited[ny][nx] = 1
                deq.append((ny, nx, i))

blank_list = deque()
blank_pipe = {}

while deq:
    y, x, direction = deq.popleft()
    if world[y][x] != '.':
        move_y, move_x, directions = move(world[y][x], direction)
        for i in range(len(move_y)):
            ny, nx = y+move_y[i], x+move_x[i]
            if 0 <= ny < r and 0 <= nx < c:
                if not visited[ny][nx] and world[ny][nx] != '.':
                    if can_enter(world[ny][nx], directions[i]):
                        visited[ny][nx] = 1
                        deq.append((ny, nx, directions[i]))
                elif world[ny][nx] == '.':
                    blank_pipe[(y, x)] = 0
                    deq.append((ny, nx, directions[i]))
                    visited[ny][nx] = 1
    else:
        for b in block_list:
            if can_enter(b, direction):
                blank_list.append((y, x, b))
for i in range(r):
    for j in range(c):
        if world[i][j] != '.' and world[i][j] != 'M' and world[i][j] != 'Z':
            if not visited[i][j]:
                for direction in pipe_direction[world[i][j]]:
                    deq.append((i, j, direction))
while deq:
    y, x, direction = deq.popleft()
    if world[y][x] != '.':
        move_y, move_x, directions = move(world[y][x], direction)
        for i in range(len(move_y)):
            ny, nx = y+move_y[i], x+move_x[i]
            if 0 <= ny < r and 0 <= nx < c:
                if not visited[ny][nx] and world[ny][nx] != '.':
                    if can_enter(world[ny][nx], directions[i]):
                        visited[ny][nx] = 1
                        deq.append((ny, nx, directions[i]))
                elif world[ny][nx] == '.':
                    blank_pipe[(y, x)] = 0
                    deq.append((ny, nx, directions[i]))
                    visited[ny][nx] = 1
    else:
        for b in block_list:
            if can_enter(b, direction):
                blank_list.append((y, x, b))

res = []
while blank_list:
    y, x, block = blank_list.popleft()
    find = True
    for direction in pipe_direction[block]:
        move_y, move_x, directions = move(block, direction)
                    
        for i in range(len(move_y)):
            ny, nx = y+move_y[i], x+move_x[i]
            if 0 <= ny < r and 0 <= nx < c:
                if not (ny, nx) in blank_pipe:
                    find = False
                    break
                if blank_pipe[(ny, nx)] == 0:
                    if can_enter(world[ny][nx], directions[i]):
                        blank_pipe[(ny, nx)] = 1
            else:
                find = False
                break

    for key in blank_pipe:
        if blank_pipe[key]:
            continue
        else:
            for key in blank_pipe:
                blank_pipe[key] = 0
            find = False 
    
    if find:
        for key in blank_pipe:
                blank_pipe[key] = 0
        res = [y+1, x+1, block]
                    

for i in res:
    print(i, end=" ")