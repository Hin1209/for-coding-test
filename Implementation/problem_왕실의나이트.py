# -*- coding: utf-8 -*-


column = [1, 2, 3, 4, 5, 6, 7, 8] # 안쓰는 리스트 굳이 만들지 않기
row = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
move = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
n = input()
count = 0 # 움직일 수 있는 경우의 수
for i in range(len(row)):
    if(n[0] == row[i]):
        pos = [(i+1), int(n[1])]
for i in range(len(move)):
    nx, ny = pos[0] + move[i][0], pos[1] + move[i][1]
    if(1 <= nx <= 8 and 1 <= ny <= 8): # 파이썬만 수학식으로 표현 가능. 자바나 씨쁠에서는 nx >= 1 and nx <= 8 이런 식으로 써야함.
        count += 1 # 이동한 결과가 판 밖이 아니면 카운트 해줌.
print(count)
