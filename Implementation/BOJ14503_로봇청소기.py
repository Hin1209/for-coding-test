n, m = list(map(int, input().split()))
posy, posx, dirc = list(map(int, input().split()))

def turn_left():
    global dirc
    if dirc != 0:
        dirc -= 1
    elif dirc == 0:
        dirc = 3



direction = [0, 1, 2, 3]
mapp = []
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
clean = 1
cnt_turn = 0

for i in range(n):
    mapp.append(list(map(int, input().split())))
mapp[posy][posx] = 2
while True:

    if cnt_turn == 4:
        nx = posx - dx[dirc]
        ny = posy - dy[dirc]
        if(0 <= nx < m and 0 <= ny < n):
            if(mapp[ny][nx] == 1):
                break
            else:
                posx = nx
                posy = ny
                cnt_turn = 0

    else:
        turn_left()
        cnt_turn += 1
        nx = posx + dx[dirc]
        ny = posy + dy[dirc]
        if(0 <= nx < m and 0 <= ny < n):
            if(mapp[ny][nx] == 0):
                clean += 1
                posx = nx
                posy = ny
                mapp[ny][nx] = 2
                cnt_turn = 0
print(clean)
