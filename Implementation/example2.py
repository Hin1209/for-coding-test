# -*- coding: utf-8 -*-

sec = 0
min = 0
hor = 0
count = 0
n = int(input())
for hor in range(n+1):
    for min in range(60):
        for sec in range(60):
            if('3' in str(sec) or '3' in str(min) or '3' in str(hor)): # str(sec) + str(min) + str(hor) 로 표현해도 됨.
                count += 1
print(count)