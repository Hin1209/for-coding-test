# -*- coding: utf-8 -*-

n = int(input())
num = n
check = 0 # 자릿수 세기
while num != 0:
    num //= 10
    check += 1
left = 0 # 왼쪽 숫자 합
right = 0 # 오른쪽 숫자 합
for _ in range(int(check/2)):
    right += n % 10
    n //= 10
for _ in range(int(check/2)):
    left += n % 10
    n //= 10
if(right == left): # 왼쪽 숫자 합과 오른쪽 숫자 합이 같으면 럭키, 다르면 레디 출력
    print("LUCKY")
else:
    print("READY")