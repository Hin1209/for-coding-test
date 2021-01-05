#숫자 카드 게임
n, m = map(int, input().split())
a = []
#각 줄의 데이터를 리스트 형태로 받아와 sort로 정렬시킴
for i in range(n):
#다른 방법으로는 sort로 정렬시키지 않고 각 줄에 대하여 min 함수를 이용해 최솟값을 찾고, max 함수를 이용해 그 중 최댓값을 찾는 방법이 있음.
    a.append(list(map(int, input().split())))
    a[i].sort()


#정렬시킨 리스트들의 첫번째 원소가 각 줄의 가장 작은 원소이므로 그 중에서 가장 큰 원소를 구함
max = 0
for i in range(n):
    if(max < a[i][0]):
        max = a[i][0]
print(max)
