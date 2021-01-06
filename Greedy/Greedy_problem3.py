# -*- coding: utf-8 -*-

#문자열 뒤집기
#시간안에도 풀었고 채점 결과 맞긴했지만 코드 길이에 아쉬움이 남는 코드
n = input()
zero_cnt = 0 #0이 나오는 구간의 개수
one_cnt = 0 #1이 나오는 구간의 개수
zero_lock = 0 #0구간 확인을 위한 잠금장치
one_lock = 0 #1구간 확인을 위한 잠금장치
for i in range(len(n)):
    if(int(n[i]) == 0 and zero_lock == 0): #0이 처음으로 나왔을때 더이상 0은 인식하지 못하게 잠금
        zero_lock = 1
        if(i == len(n)-1): #문자열이 0으로 끝나 구간 개수를 카운트 하지 못하는 예외 상황 처리
            zero_cnt += 1
    elif(int(n[i]) == 1 and zero_lock == 1): #잠금이 되어있는 상태에서 1이 나오면 구간 개수를 +1 해주고 0을 찾기위해 잠금을 품
        zero_cnt += 1
        zero_lock = 0
    if(zero_lock == 1 and i == len(n)-1): #문자열이 0으로 끝나 구간 개수를 카운트 하지 못하는 예외 상황 처리
        zero_cnt += 1
    if (int(n[i]) == 1 and one_lock == 0): #위 코드에서 0과 1만 바꿈
        one_lock = 1
        if(i == len(n)-1):
            one_cnt += 1
    elif (int(n[i]) == 0 and one_lock == 1):
        one_cnt += 1
        one_lock = 0
    if (one_lock == 1 and i == len(n) - 1):
        one_cnt += 1
print(min(one_cnt, zero_cnt)) #0구간과 1구간 중 적은 것을 선택


#답지 코드
# count0 = 0
# count1 = 0
#
# if(n[0] == '1'):
#     count0 += 1
# else:
#     count1 += 1
#
# for i in range(len(n)-1):
#     if(n[i] != n[i+1]):
#         if(n[i+1] == '1'):
#             count0 += 1
#         else:
#             count1 += 1
# print(min(count0, count1))
