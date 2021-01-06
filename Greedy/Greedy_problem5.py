# -*- coding: utf-8 -*-
import sys
n, m = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
data.sort()
count = n * (n-1) / 2
weight = [0 for i in range(m+1)]
for i in range(n):
    weight[data[i]] += 1
for i in range(1, m+1):
    if(weight[i] > 1):
        count -= weight[i] * (weight[i]-1) / 2
print(count)
