import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
cnt_pre_course = [0] * (N + 1)
pre_course = [[] for _ in range(N + 1)]
course_time = [0] * (N + 1)
d = deque()

for i in range(1, N + 1):
    tmp = list(map(int, input().split()))
    course_time[i] = tmp[0]
    for j in range(1, len(tmp) - 1):
        pre_course[tmp[j]].append(i)
        cnt_pre_course[i] += 1

for i in range(1, N + 1):
    if cnt_pre_course[i] == 0:
        d.append((i, course_time[i]))

while d:
    cos, time = d.popleft()
    for i in pre_course[cos]:
        cnt_pre_course[i] -= 1
        if cnt_pre_course[i] == 0:
            d.append((i, course_time[i] + time))
    print(time)
