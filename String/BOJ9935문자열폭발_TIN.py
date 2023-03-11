import sys
sys.setrecursionlimit(10**7)

input = sys.stdin.readline

string = input().rstrip()
boom = input().rstrip()
stack = []

for i in range(len(string)):
    stack.append(string[i])
    bang = False
    if len(stack) >= len(boom):
        bang = True
        for j in range(len(boom)):
            index = len(stack) - len(boom) + j
            if stack[index] != boom[j]:
                bang = False
                break
    if bang:
        for j in range(len(boom)):
            stack.pop()
        continue

if stack:
    for i in stack:
        print(i, end="")
else:
    print("FRULA")