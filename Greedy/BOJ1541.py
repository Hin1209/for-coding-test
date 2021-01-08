# -*- coding: utf-8 -*-
# 실버 2
import sys
n = sys.stdin.readline()
plus_index = [] # + 나오는 위치 저장
minus_index = [] # - 나오는 위치 저장
count = 1 # + - 위치 파악
open = 0 # 괄호 열기
for i in range(len(n)):
    if(n[i] == '+'):
        plus_index.append(count)
        count += 1 # 부호가 나올때마다 count 올려주고 인덱스 저장하는 리스트에 추가
    elif(n[i] == '-'):
        minus_index.append(count)
        count += 1
n = n.split('+') # + 로 먼저 나눠줌
lis = [] # - 까지 스플릿해서 저장할 리스트
num_list = [] # 숫자만 담을 리스트
for i in range(len(n)):
   lis.append(n[i].split('-')) # lis에 n의 모든 원소들을 - 로 스플릿한 결과를 담음
for i in range(len(lis)):
    for j in range(len(lis[i])):
        num_list.append(list(map(int, lis[i][j].split()))) # lis에 [[34], [23 54], [43 54 64]] 이런식으로 저장되는데 숫자만 모두 빼내기 위한 코드
f_num = num_list[0][0] # 처음 시작하는 숫자
minus = 0 # 빼줄 숫자
for i in range(1, len(num_list)):
    if(i in minus_index and open == 0): # - 부호가 처음으로 나오면(open == 0) minus에 숫자를 추가하고 괄호를 열어줌(open = 1)
        minus += num_list[i][0]
        open = 1
    elif(open == 1): # - 부호 이후에 나오는 숫자는 모두 빼줌
        minus += num_list[i][0]
    elif(i in plus_index and open == 0): # 나머지 경우는 -가 나오기 전에 +만 나오는 구간이므로 결과값에 계속 더함
        f_num += num_list[i][0]
    if (i == len(num_list) - 1): # 괄호가 닫히지 않은 상태로 끝나면 지금까지 나온 minus들을 빼주고 마무리함
        f_num -= minus
print(f_num)
