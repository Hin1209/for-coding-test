import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    selected = [0] + list(map(int, input().split()))
    visited = [0] * (n+1)
    
    for i in range(1, n+1):
        if visited[i] == 0:
            if i == selected[i]:
                visited[i] = 1
            else:
                can_team = []
                next = i
                success = False
                visit = 1
                can_team.append(next)
                visited[next] = visit
                while True:
                    if (visited[selected[next]] != 0 and selected[next] not in can_team) or visited[selected[next]] == -1:
                        break
                    if len(can_team) > 0 and selected[next] == can_team[0]:
                        can_team.append(next)
                        visited[next] = visit
                        success = True
                        break
                    elif next != selected[next]:
                        if visited[selected[next]] != 0:
                            index = visited[selected[next]] - 1
                            for j in range(index):
                                visited[can_team[j]] = -1
                            for j in range(index, len(can_team)):
                                visited[can_team[j]] = j - index + 1
                            success = True
                            break
                        visit += 1
                        next = selected[next]
                        visited[next] = visit
                        can_team.append(next)
                    elif next == selected[next]:
                        can_team.pop()
                        break
                if not success:
                    for j in can_team:
                        visited[j] = -1
    cnt = 0
    for i in range(1, n+1):
        if visited[i] == -1:
            cnt += 1
    print(cnt)