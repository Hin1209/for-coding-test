# -*- coding: utf-8 -*-

n, m = list(map(int, input().split()))
posy, posx, dirc = list(map(int, input().split()))
count = 0
mapp = []
dx = [0, 0, 1, -1] # dx = [-1, 0, 1, 0]
dy = [1, -1, 0, 0] # dy = [0, 1, 0, -1] direction이 0,1,2,3 이므로 그에 맞게 dx, dy 설정
for i in range(m):
    mapp.append(list(map(int, input().split())))
mapp[posy][posx] = 1
count += 1
stop = 0
while True:
    if(dirc == 0):
        lefx = posx + dx[3]
        lefy = posy
        if(lefx >= 0 and lefx < m and lefy >= 0 and lefy < n):
            if(mapp[lefy][lefx] == 0):
                mapp[lefy][lefx] = 2
                posx = lefx
                posy = lefy
                dirc = 3 # turn_left 함수를 짜자
                count += 1
                stop = 0
            else:
                stop += 1
                if (stop == 4):
                    bacx = posx
                    bacy = posy + dy[0]
                    if (mapp[bacy][bacx] == 1):
                        break
                    else:
                        posx = bacx
                        posy = bacy
                        # count += 1 이미 방문한 칸은 세지 않음
                        continue
                dirc = 3

    elif(dirc == 1):
        lefx = posx
        lefy = posy + dy[1]
        if (lefx >= 0 and lefx < m and lefy >= 0 and lefy < n):
            if (mapp[lefy][lefx] == 0):
                mapp[lefy][lefx] = 2
                posx = lefx
                posy = lefy
                dirc = 0
                count += 1
                stop = 0
            else:
                stop += 1
                if (stop == 4):
                    bacx = posx + dx[3]
                    bacy = posy
                    if (mapp[bacy][bacx] == 1):
                        break
                    else:
                        posx = bacx
                        posy = bacy
                        # count += 1
                        continue
                dirc = 0

    elif(dirc == 2):
        lefx = posx + dx[2]
        lefy = posy
        if (lefx >= 0 and lefx < m and lefy >= 0 and lefy < n):
            if (mapp[lefy][lefx] == 0):
                mapp[lefy][lefx] = 2
                posx = lefx
                posy = lefy
                dirc = 1
                count += 1
                stop = 0
            else:
                stop += 1
                if (stop == 4):
                    bacx = posx
                    bacy = posy + dy[1]
                    if (mapp[bacy][bacx] == 1):
                        break
                    else:
                        posx = bacx
                        posy = bacy
                        # count += 1
                        continue
                dirc = 1

    elif(dirc == 3):
        lefx = posx
        lefy = posy + dy[0]
        if (lefx >= 0 and lefx < m and lefy >= 0 and lefy < n):
            if (mapp[lefy][lefx] == 0):
                mapp[lefy][lefx] = 2
                posx = lefx
                posy = lefy
                dirc = 2
                count += 1
                stop = 0
            else:
                stop += 1
                if(stop == 4):
                    bacx = posx + dx[2]
                    bacy = posy
                    if(mapp[bacy][bacx] == 1):
                        break
                    else:
                        posx = bacx
                        posy = bacy
                        # count += 1
                        continue
                dirc = 2
print(count)