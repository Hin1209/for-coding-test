import sys

input = sys.stdin.readline

def union_team(student, a, b):
    a = find_team(student, a)
    b = find_team(student, b)
    if a < b:
        student[b] = a
    else:
        student[a] = b

def find_team(student, a):
    if student[a] != a:
        student[a] = find_team(student, student[a])
    return student[a]

N, M = map(int, input().split())

student = [0] * (N + 1)

for i in range(N + 1):
    student[i] = i

for _ in range(M):
    act, a, b = map(int, input().split())
    if act == 1:
        if find_team(student, a) == find_team(student, b):
            print("YES")
        else:
            print("NO")
    else:
        union_team(student, a, b)
