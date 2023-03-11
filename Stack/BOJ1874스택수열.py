import sys

input = sys.stdin.readline

n = int(input())

stack = []
numbers = []
target = []
res = []
cnt = 1

for _ in range(n):
    tmp = int(input())
    target.append(tmp)

possible = True
for num in target:
    if len(numbers) == 0:
        numbers.append(cnt)
        cnt += 1
        res.append('+')
    while numbers[-1] < num:
        numbers.append(cnt)
        cnt += 1
        res.append('+')
    if numbers[-1] == num:
        res.append('-')
        numbers.pop()
    elif numbers[-1] > num:
        possible = False
    
if possible:
    for i in res:
        print(i)
else:
    print("NO")
