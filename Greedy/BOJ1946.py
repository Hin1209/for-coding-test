# -*- coding: utf-8 -*-

import sys
t = int(sys.stdin.readline())

for _ in range(t):
    dic = set()
    apl = [] #신입사원들의 점수를 담을 리스트
    count = 1 #맨 위에 오는 신입사원을 뽑는다는 기준으로 처음에 1로 시작함
    n = int(sys.stdin.readline())
    for _ in range(n):
        a = tuple(map(int, sys.stdin.readline().split())) #신입사원들의 점수를 튜플 형태로 저장
        apl.append(a)
    apl.sort(key = lambda x : x[0]) #신입사원들의 서류 점수를 기준으로 오름차순 정렬 시킴
    min = apl[0][1] #서류 점수가 가장 낮은 신입사원의 면접 점수를 최솟값으로 설정
    for i in range(1,n):
        if(apl[i][1] < min): #설정한 최솟값보다 작은 면접 점수가 나오면 문제 조건을 만족하므로 뽑는 형식. 최솟값은 그 사원의 면접 점수로 초기화시킴
            min = apl[i][1]
            count += 1
    print(count)
