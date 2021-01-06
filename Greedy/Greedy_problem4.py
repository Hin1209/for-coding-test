# -*- coding: utf-8 -*-


n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1 # 숫자 1은 만들 수 있다고 가정
if(target != data[0]):

    print(1) # 못 만들면 1 출력
else:
    for i in range(1, n):
        if target+1 < data[i]: # 1~target 까지는 만들 수 있는 수, 다음 원소가 target 보다 1만큼 크다면 1~target+data[i]까지 만들 수 있음.
            print(target+1) # 반면에 원소가 target과 2이상 차이가 나는 순간 target+1 부터 data[i]-1까지의 숫자를 만들 수 없게 됨.그래서 최솟값이 target+1
            break
        else:
            target += data[i]

# 답지에서는 인덱스 0번 숫자부터 고려해줌 -> 만드려고 목표하는 수가 target인 반면 위의 코드에서는 만들수 있는 숫자까지가 target임.
# 그래서 위의 코드와 아래 코드의 target이 1이 차이가 남
# target = 1
# for i in data:
#     if target < i:
#         print(target)
#         break
#     target += i



# 매번 리스트를 n^2번 돌리게되니 시간이 너무 오래 걸림
# max_sum = sum(data)
# check = 0
# for i in range(1, max_sum+1):
#     check = 0
#     for j in range(n):
#         for k in range(j+1, n):
#             if(i == sum(data[j:k])):
#                 check = 1
#     if(check == 0):
#         print(i)
#         break

