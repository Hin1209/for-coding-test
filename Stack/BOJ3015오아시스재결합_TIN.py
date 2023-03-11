import sys

input = sys.stdin.readline

n = int(input())
stack = []
cnt = 0
same = {}
for _ in range(n):
    person = int(input())
    if person in same.keys():
        if same[person] == 0:
            same[person] = 1
    else:
        same[person] = 1
    while stack:
        if stack[-1] < person:
            small = stack.pop()
            cnt += same[small]
            same[small] = 0
        elif stack[-1] == person:
            cnt += same[stack.pop()]
            same[person] += 1
        else:
            cnt += 1
            break
    stack.append(person)
print(cnt)