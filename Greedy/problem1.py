# -*- coding: utf-8 -*-

#큰 수의 법칙
import sys
n, m, k = map(int, input().split())
data = list(map(int, input().split()))
max = data[0]
second_max = data[0]
sum = 0

#가장 큰 수와 두번째로 큰 수를 구해주는 과정
#sort 메소드를 이용하여 리스트를 정렬한 다음 마지막 원소와 그 직전 원소만 뽑아오는 방법도 있음.(시간 복잡도 down)
for i in range(n):
    if(max < data[i]):
        max = data[i]
for i in range(n):
    if(second_max < data[i] and data[i] < max):
        second_max = data[i]

cnt = 0
#가장 큰 수가 오직 하나일 때와 두개일때를 나눠서 생각해줌. 다른 방법으로 while문을 이용해 안에서 for문을 한번 더 돌리면서 m을 감소시켜 0이 될때까지 반복하는
#방법이 있음.
for i in range(n):
    if(data[i] == max):
        cnt += 1
if(cnt == 1):
    # (가장 큰 수+두번째로 큰 수)가 반복되는 횟수를 구하고 마지막에 가장 큰 수만 더해지는 횟수를 구해 계산해줌.
    sum = (k*max+second_max) * (m//(k+1)) + max * (m%(k+1))
else:
    sum = max * m

print(sum)
