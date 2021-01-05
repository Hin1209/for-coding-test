#모험가 길드
import time
n = int(input())
ad = list(map(int, input().split()))
start = time.time()
group = []
ad.sort()
stop = 0
while(True):
    #tmp에 임시 그룹을 저장함
    tmp = []
    #l에 남은 모험가 수를 저장
    l = len(ad)
    #남은 모험가가 없거나 모험가의 최소 공포도가 남은 인원보다 적을때 종료
    if(l == 0 or min(ad) > l):
        break
    #위 조건을 통과하면 그룹이 만들어질수 있으므로 최소 공포도를 가진 모험가를 tmp에 넣음
    tmp.append(ad.pop(0))
    #공포도가 1인 경우는 바로 그룹에 포함
    if(tmp[0] != 1):
        #tmp에서 공포도의 최댓값이 tmp에 들어간 인원과 동일해질때까지 반복
        while(max(tmp) != len(tmp)):
            tmp.append(ad.pop(0))
            #예외 문항. ad에서 공포도의 최솟값이 ad의 크기보다 작음에도 불구하고, 남은 인원들의 공포도가 너무 높아 그룹 결성이 불가능한 경우 while문 탈출
            if(len(ad) == 0):
                stop = 1
                break
    if(stop == 1):
        break
    group.append(tmp)

print(len(group))
end = time.time()
print(end - start)





#시간 내에 다 못푼 코드
#위의 코드와는 달리 공포도가 높은 인원부터 그룹에 포함시켜버림
# group = 0
# while(True):
#     cnt = 0
#     for i in range(len(ad)):
#         if(ad[i] <= len(ad)):
#             cnt += 1
#     if (len(ad) == 0 or cnt == 0):
#         break
#     elif(ad[-1] <= len(ad)):
#         group += 1
#         for i in range(ad[-1]):
#             ad.pop(-1)
#     elif(ad[-1] > len(ad)):
#         for i in range(len(ad)):
#             if(ad[len(ad)-i-1] < len(ad)):
#                 group += 1
#                 for j in range(ad[len(ad)-i-1]):
#                     ad.pop(-1)
# print(group)

#답지 코드
# result = 0
# count = 0
#
# for i in ad:
#     count += 1
#     if count >= i:
#         result += 1
#         count = 0
# print(result)
