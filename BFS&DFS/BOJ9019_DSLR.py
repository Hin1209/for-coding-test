import sys
from collections import deque

input = sys.stdin.readline


def D(target):
    target *= 2
    if target > 9999:
        target %= 10000
    return target


def S(target):
    if target == 0:
        return 9999
    target -= 1
    return target


def L(target):
    target = (target % 1000) * 10 + target // 1000
    return target


def R(target):
    target = (target % 10) * 1000 + target // 10
    return target


T = int(input())

for _ in range(T):
    A, B = list(map(int, input().split()))
    d = deque()
    d.append((A, ""))
    visited = [False] * 10001
    visited[A] = True

    while d:
        num, command = d.popleft()
        if num == B:
            print(command)
            break
        Dnum = D(num)
        Snum = S(num)
        Lnum = L(num)
        Rnum = R(num)
        if not visited[Dnum]:
            d.append((Dnum, command + "D"))
            visited[Dnum] = True
        if not visited[Snum]:
            d.append((Snum, command + "S"))
            visited[Snum] = True
        if not visited[Lnum]:
            d.append((Lnum, command + "L"))
            visited[Lnum] = True
        if not visited[Rnum]:
            d.append((Rnum, command + "R"))
            visited[Rnum] = True
