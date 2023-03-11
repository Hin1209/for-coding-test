import sys
input = sys.stdin.readline

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

a = [x1, y1]
b = [x2, y2]
c = [x3, y3]
d = [x4, y4]

def ccw(p1, p2, p3):
    res = (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p3[0] - p1[0]) * (p2[1] - p1[1])
    if res > 0:
        return 1
    elif res < 0:
        return -1
    else:
        return 0

abc = ccw(a,b,c)
abd = ccw(a,b,d)
cda = ccw(c,d,a)
cdb = ccw(c,d,b)
if a[0] == b[0] and b[0] == c[0] and c[0] == d[0]:
    if a[1] > b[1]:
        a[1], b[1] = b[1], a[1]
    if c[1] > d[1]:
        c[1], d[1] = d[1], c[1]
    if a[1] <= d[1] and c[1] <= b[1]:
        print(1)
    else:
        print(0)
else:
    if abc * abd == 0 and cda * cdb == 0:
        if a[0] > b[0]:
            a[0], b[0] = b[0], a[0]
        if c[0] > d[0]:
            c[0], d[0] = d[0], c[0]
        if a[0] <= d[0] and c[0] <= b[0]:
            print(1)
        else:
            print(0)
    elif abc * abd <= 0 and cda * cdb <= 0:
        print(1)
    else:
        print(0)