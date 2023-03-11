import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

world = []
for _ in range(n):
    world.append(input().rstrip())
    
for i in range(n):
    for j in range(m):
        if world[i][j] == "R":
            red = [i, j]
        if world[i][j] == "B":
            blue = [i, j]
        if world[i][j] == "O":
            goal = (i, j)
deq = deque()
deq.append((red[0], red[1], blue[0], blue[1], 0))
res = 11
while deq:
    ry, rx, by, bx, cnt = deq.popleft()
    if cnt == 10:
        continue
    for i in range(4):
        prx = rx
        pry = ry
        pbx = bx
        pby = by
        fail = False
        success = False
        if i == 0:
            if prx < pbx:
                while True:
                    next = prx - 1        
                    if 0 < next and world[pry][next] != "#":
                        if world[pry][next] == "O":
                            success = True
                            prx -= 1
                            break
                        prx -= 1
                    elif world[pry][next] == "#":
                        break
                while True:
                    next = pbx - 1
                    if 0 < next and world[pby][next] != "#":
                        if world[pby][next] == "O":
                            fail = True
                            break
                        if pry == pby and next == prx:
                            break
                        pbx -= 1 
                    elif world[pby][next] == "#":
                        break
                if not fail:
                    if prx == rx and pry == ry and pbx == bx and pby == by:
                        continue
                    elif success:
                        res = min(res, cnt+1)
                        continue
                    deq.append((pry, prx, pby, pbx, cnt+1))
            else:
                while True:
                    next = pbx - 1
                    if 0 < next and world[pby][next] != "#":
                        if world[pby][next] == "O":
                            fail = True
                            break
                        pbx -= 1 
                    elif world[pby][next] == "#":
                        break
                while True:
                    next = prx - 1        
                    if 0 < next and world[pry][next] != "#":
                        if pry == pby and next == pbx:
                            break
                        if world[pry][next] == "O":
                            success = True
                            prx -= 1
                            break
                        prx -= 1
                    elif world[pry][next] == "#":
                        break
                if not fail:
                    if prx == rx and pry == ry and pbx == bx and pby == by:
                        continue
                    elif success:
                        res = min(res, cnt+1)
                        continue
                    deq.append((pry, prx, pby, pbx, cnt+1))
        elif i == 1:
            if prx > pbx:
                while True:
                    next = prx + 1        
                    if next < m and world[pry][next] != "#":
                        if world[pry][next] == "O":
                            success = True
                            prx += 1
                            break
                        prx += 1
                    elif world[pry][next] == "#":
                        break
                while True:
                    next = pbx + 1
                    if next < m and world[pby][next] != "#":
                        if world[pby][next] == "O":
                            fail = True
                            break
                        if pry == pby:
                            if next == prx:
                                break
                        pbx += 1 
                    elif world[pby][next] == "#":
                        break
                if not fail:
                    if prx == rx and pry == ry and pbx == bx and pby == by:
                        continue
                    elif success:
                        res = min(res, cnt+1)
                        continue
                    deq.append((pry, prx, pby, pbx, cnt+1))
            else:
                while True:
                    next = pbx + 1
                    if next < m and world[pby][next] != "#":
                        if world[pby][next] == "O":
                            fail = True
                            break
                        pbx += 1 
                    elif world[pby][next] == "#":
                        break
                while True:
                    next = prx + 1        
                    if next < m and world[pry][next] != "#":
                        if pry == pby and next == pbx:
                            break
                        if world[pry][next] == "O":
                            success = True
                            prx += 1
                            break
                        prx += 1
                    elif world[pry][next] == "#":
                        break
                if not fail:
                    if prx == rx and pry == ry and pbx == bx and pby == by:
                        continue
                    elif success:
                        res = min(res, cnt+1)
                        continue
                    deq.append((pry, prx, pby, pbx, cnt+1))
        elif i == 2:
            if pry < pby:
                while True:
                    next = pry - 1        
                    if 0 < next and world[next][prx] != "#":
                        if world[next][prx] == "O":
                            success = True
                            pry -= 1
                            break
                        pry -= 1
                    elif world[next][prx] == "#":
                        break
                while True:
                    next = pby - 1
                    if 0 < next and world[next][pbx] != "#":
                        if world[next][pbx] == "O":
                            fail = True
                            break
                        if prx == pbx and next == pry:
                            break
                        pby -= 1 
                    elif world[next][pbx] == "#":
                        break
                if not fail:
                    if prx == rx and pry == ry and pbx == bx and pby == by:
                        continue
                    elif success:
                        res = min(res, cnt+1)
                        continue
                    deq.append((pry, prx, pby, pbx, cnt+1))
            else:
                while True:
                    next = pby - 1
                    if 0 < next and world[next][pbx] != "#":
                        if world[next][pbx] == "O":
                            fail = True
                            break
                        pby -= 1 
                    elif world[next][pbx] == "#":
                        break
                while True:
                    next = pry - 1        
                    if 0 < next and world[next][prx] != "#":
                        if prx == pbx and next == pby:
                            break
                        if world[next][prx] == "O":
                            success = True
                            pry -= 1
                            break
                        pry -= 1
                    elif world[next][prx] == "#":
                        break
                if not fail:
                    if prx == rx and pry == ry and pbx == bx and pby == by:
                        continue
                    elif success:
                        res = min(res, cnt+1)
                        continue
                    deq.append((pry, prx, pby, pbx, cnt+1))
        elif i == 3:
            if pry > pby:
                while True:
                    next = pry + 1        
                    if next < n and world[next][prx] != "#":
                        if world[next][prx] == "O":
                            success = True
                            pry += 1
                            break
                        pry += 1
                    elif world[next][prx] == "#":
                        break
                while True:
                    next = pby + 1
                    if next < n and world[next][pbx] != "#":
                        if world[next][pbx] == "O":
                            fail = True
                            break
                        if prx == pbx and next == pry:
                            break
                        pby += 1 
                    elif world[next][pbx] == "#":
                        break
                if not fail:
                    if prx == rx and pry == ry and pbx == bx and pby == by:
                        continue
                    elif success:
                        res = min(res, cnt+1)
                        continue
                    deq.append((pry, prx, pby, pbx, cnt+1))
            else:
                while True:
                    next = pby + 1
                    if next < n and world[next][pbx] != "#":
                        if world[next][pbx] == "O":
                            fail = True
                            break
                        pby += 1 
                    elif world[next][pbx] == "#":
                        break
                while True:
                    next = pry + 1        
                    if next < n and world[next][prx] != "#":
                        if prx == pbx and next == pby:
                            break
                        if world[next][prx] == "O":
                            success = True
                            pry += 1
                            break
                        pry += 1
                    elif world[next][prx] == "#":
                        break
                if not fail:
                    if prx == rx and pry == ry and pbx == bx and pby == by:
                        continue
                    elif success:
                        res = min(res, cnt+1)
                        continue
                    deq.append((pry, prx, pby, pbx, cnt+1))
if res == 11:
    print(-1)
else:
    print(res)