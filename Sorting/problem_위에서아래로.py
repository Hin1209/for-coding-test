# -*- coding: utf-8 -*-

n = int(input())
array = []
for i in range(n):
    array.append(int(input()))
array.sort(reverse = True)
for i in range(n):
    print(array[i], end = ' ') # print는 기본적으로 끝나고 줄바꿈을 하는데, end를 직접 설정해주어 줄바꿈 대신 띄어쓰기를 한다. 