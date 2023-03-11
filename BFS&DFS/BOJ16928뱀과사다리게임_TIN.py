import sys
from collections import deque

input = sys.stdin.readline

up, down = map(int, input().split())

move = {}
snake = {}
world = [9000 for i in range(101)]

for i in range(up):
    st, ed = map(int, input().split())
    move[st] = ed

for i in range(down):
    st, ed = map(int, input().split())
    snake[st] = ed

state = deque() 
state.append((1,0))

while(state):
    pos, cnt = state.popleft()
    if pos >= 100:
        continue
    if pos in move.keys():
        if world[move[pos]] == 9000 or world[move[pos]] > cnt:
            state.append((move[pos], cnt))
            world[move[pos]] = cnt
        world[pos] = 9000
    if pos in snake.keys():
        if world[snake[pos]] == 9000 or world[snake[pos]] > cnt:
            state.append((snake[pos],cnt))
            world[snake[pos]] = cnt
        world[pos] = 9000
    else:
        for i in range(1,7):
            next = pos + i
            if next > 100:
                break
            if world[next] == 9000 or world[next] > cnt + 1:
                state.append((next,cnt+1))
                world[next] = cnt + 1 
        
print(world[100])