# -*- coding: utf-8 -*-
#실버3
import sys
n = int(sys.stdin.readline())
array = list(map(int, sys.stdin.readline().split()))
array.sort() #인출 시간이 짧은 사람이 앞에 올수록 시간이 적게 걸림
sum = 0
for i in range(n):
    sum += array[i] * (n-i)
print(sum)
