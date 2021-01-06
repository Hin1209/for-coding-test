# -*- coding: utf-8 -*-

n = int(input())
count = 0
unit = [500, 100, 50, 10]
for i in unit:
    if(n // i != 0):
        count += n//i
        n -= (n//i) * i #n %= i로 표현도 가능

print(count)