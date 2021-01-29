# -*- coding: utf-8 -*-

n = input()
alpa = [] # 알파벳 저장할 리스트
num = [] # 숫자 저장할 리스트
nsum = 0 # 숫자들 합계
num_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'] # 숫자와 알파벳을 구분하기 위해 미리 만듬

result = ''
for i in range(len(n)):
    if(n[i] in num_list): # 입력값의 원소 중 숫자가 있으면 num 리스트에 int 형으로 저장
        num.append(int(n[i]))
    else:
        alpa.append(n[i]) # 나머지는 알파벳이기 때문에 alpa에 저장
nsum = sum(num) # 숫자들 합계 구하기
alpa.sort() # 알파벳 순서 정렬
for i in range(len(alpa)):
    result += alpa[i] # 정렬한 알파벳들 먼저 result에 추가
result += str(nsum) # 숫자들 합계 string 으로 변환해서 추가
print(result)


# 나중에 해결해 볼 것 -> sort 메소드 말고는 알파벳을 정렬할 방법이 뭐가 있을까?