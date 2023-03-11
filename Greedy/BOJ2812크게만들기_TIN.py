import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, k = map(int, input().split())
num = input().rstrip()

res = []
res.append(int(num[0]))
cnt = 0


for i in range(1, len(num)):
    # 반복문 종료 조건 - 주어진 개수만큼 지운 경우
    if cnt == k:
        for j in range(i, len(num)):
            res.append(int(num[j]))
        break
    
    target = int(num[i])
    # 현재 숫자가 스택의 마지막 숫자보다 큰 경우
    if target > res[-1]:
        # 스택에서 현재 숫자보다 크거나 같은 숫자가 나올떄까지, 혹은 목표 개수만큼 채울때까지 스택에서 숫자를 지운다.
        while len(res) > 0 and target > res[-1]:
            res.pop()
            cnt += 1
            if cnt == k:
                break
        res.append(target)
    # 스택의 마지막 숫자가 현재 숫자보다 크거나 같은 경우 넘어감
    else:
        res.append(target)
        
# 목표 개수만큼 지우지 못했을때 뒤의 숫자를 지운다.
if cnt < k:
    while cnt != k:
        res.pop()
        cnt += 1
        
str_res = ''
for i in res:
    str_res += str(i)

print(str_res)