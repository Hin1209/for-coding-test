import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    operator = input().rstrip()
    N = int(input())
    s_tmp = input().rstrip()
    q = deque()
    tmp = ''

    if s_tmp == "[]":
        if "D" in operator:
            print("error")
            continue
        else:
            print("[]")
            continue

    for i in range(len(s_tmp)):
        if s_tmp[i].isalnum():
            tmp += s_tmp[i]
        elif s_tmp[i] == ",":
            q.append(int(tmp))
            tmp = ''
    if tmp:
        q.append(int(tmp))

    error = 0
    reverse = 0

    for i in range(len(operator)):
        if operator[i] == "R" and reverse == 0:
            reverse = 1
        elif operator[i] == "R" and reverse != 0:
            reverse = 0
        elif operator[i] == "D":
            if len(q) == 0:
                print("error")
                error = 1
                break
            elif reverse == 1:
                q.pop()
            else:
                q.popleft()

    l = len(q)

    if not error:
        print("[", end = '')
        for i in range(l):
            if reverse:
                if i == l - 1:
                    print(q.pop(), end = "]")
                else:
                    print(q.pop(), end=",")
            else:
                if i == l - 1:
                    print(q.popleft(), end = "]")
                else:
                    print(q.popleft(), end = ",")
        if l == 0:
            print("]", end = '')
        print()




