# -*- coding: utf-8 -*-
import sys
n, m = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
data.sort()
count = n * (n-1) / 2 #모든 볼링공 중에서 두개만 선택하는 경우의 수
weight = [0 for i in range(m+1)] #각 무게별로 공이 몇개씩 있는지 저장하는 리스트
for i in range(n):
    weight[data[i]] += 1
for i in range(1, m+1):
    if(weight[i] > 1):
        count -= weight[i] * (weight[i]-1) / 2 #같은 공이 두개 이상일때 같은 공을 선택하는 경우를 빼줌
print(count)
