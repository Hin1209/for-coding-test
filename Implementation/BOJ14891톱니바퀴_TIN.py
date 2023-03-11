import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

gear1 = []
gear2 = []
gear3 = []
gear4 = []

def rotate(num_gear, isClock):
    if num_gear == 1:
        tmp = gear1
    elif num_gear == 2:
        tmp = gear2
    elif num_gear == 3:
        tmp = gear3
    elif num_gear == 4:
        tmp = gear4
    if isClock:
        save = tmp[7]
        for i in range(6, -1, -1):
            tmp[i+1] = tmp[i]
        tmp[0] = save
    else:
        save = tmp[0]
        for i in range(7):
            tmp[i] = tmp[i+1]
        tmp[7] = save

def check_rotate(start, isClock):
    if start == 1:
        if gear1[2] != gear2[6]:
            if gear2[2] != gear3[6]:
                if gear3[2] != gear4[6]:
                    rotate(4, not isClock)
                rotate(3, isClock)
            rotate(2, not isClock)
        rotate(1, isClock)
    elif start == 2:
        if gear2[2] != gear3[6]:
                if gear3[2] != gear4[6]:
                    rotate(4, isClock)
                rotate(3, not isClock)
        if gear2[6] != gear1[2]:
            rotate(1, not isClock)
        rotate(2, isClock)
    elif start == 3:
        if gear3[2] != gear4[6]:
            rotate(4, not isClock)
        if gear3[6] != gear2[2]:
            if gear2[6] != gear1[2]:
                rotate(1, isClock)
            rotate(2, not isClock)
        rotate(3, isClock)
    elif start == 4:
        if gear4[6] != gear3[2]:
            if gear3[6] != gear2[2]:
                if gear2[6] != gear1[2]:
                    rotate(1, not isClock)
                rotate(2, isClock)
            rotate(3, not isClock)
        rotate(4, isClock)

for i in range(4):
    tmp = input().rstrip()
    
    for j in tmp:
        if i == 0:
            gear1.append(int(j))
        elif i == 1:
            gear2.append(int(j))
        elif i == 2:
            gear3.append(int(j))
        elif i == 3:
            gear4.append(int(j))
            
k = int(input())

for i in range(k):
    num, direction = map(int, input().split())
    if direction == 1:
        check_rotate(num, True)
    else:
        check_rotate(num, False)

res = 0
if gear1[0]:
    res += 1
if gear2[0]:
    res += 2
if gear3[0]:
    res += 4
if gear4[0]:
    res += 8
print(res)