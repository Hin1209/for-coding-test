import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
n, m, p = map(int, input().split())

s = [0] + list(map(int, input().split()))

world = [input().rstrip() for _ in range(n)]

state = [[0] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]
visited_cnt = [[0] * m for _ in range(n)]

count = [0] * (p+1)

queue = [deque() for _ in range(p+1)]
for i in range(n):
    for j in range(m):
        if world[i][j] == ".":
            continue
        elif world[i][j] == "#":
            state[i][j] = -1
        else:
            state[i][j] = int(world[i][j])
            queue[state[i][j]].append((1, i, j))
            visited[i][j] = 1


def expand(player, mv, y, x, t):
    deq = deque()
    deq.append((mv, y, x))
    while deq:
        cnt_mv, yy, xx = deq.popleft()
        for i in range(4):
            ny, nx = yy+dy[i], xx+dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if state[ny][nx] == 0:
                    state[ny][nx] = player
                    visited[ny][nx] = t+1
                    visited_cnt[ny][nx] = cnt_mv-1
                    if cnt_mv-1 > 0:
                        deq.append((cnt_mv-1, ny, nx))
                    queue[player].append((t+1, ny, nx))
                elif state[ny][nx] == player:
                    if visited[ny][nx] == t+1 and cnt_mv-1 > visited_cnt[ny][nx]:
                        visited_cnt[ny][nx] = cnt_mv-1
                        if cnt_mv-1 > 0:
                            deq.append((cnt_mv-1, ny, nx))
                elif player < state[ny][nx] and visited[ny][nx] == t+1:
                    state[ny][nx] = player
                    visited_cnt[ny][nx] = cnt_mv-1
                    if cnt_mv-1 > 0:
                        deq.append((cnt_mv-1, ny, nx))
                    queue[player].append((t+1, ny, nx))

def is_expand(queue):
    for i in range(1, len(queue)):
        if len(queue[i]) > 0:
            return True
    return False

max_mv = n+m+1

turn = 1
while is_expand(queue):
    for player in range(1, p+1):
        while queue[player]:
            time, y, x = queue[player].popleft()
            if time > turn:
                queue[player].append((time, y, x))
                break
            move = min(s[player], max_mv)
            visited_cnt[y][x] = move
            expand(player, move, y, x, time)
    turn += 1
    
for i in range(n):
    for j in range(m):
        if state[i][j] > 0:
            count[state[i][j]] += 1
   
for i in range(1,p+1):
    print(count[i], end=" ")
