# -*- coding: utf-8 -*-
import sys
n = int(sys.stdin.readline())
pos = [1, 1]
vec = sys.stdin.readline().split()
# dx, dy 이용해서 짜는 습관 들이기
for i in vec:
    if i == 'R':
        if pos[1] < n:
            pos[1] += 1
    elif i == 'L':
        if pos[1] > 1:
            pos[1] -= 1
    elif i == 'U':
        if pos[0] > 1:
            pos[0] -= 1
    elif i == 'D':
        if pos[0] < n:
            pos[0] += 1

print(pos[0], pos[1])