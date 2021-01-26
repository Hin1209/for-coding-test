import sys
import heapq

input = sys.stdin.readline
# 무한 설정
INF = int(1e9)

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
distance = [INF for _ in range(N + 1)]
for _ in range(M):
    start, end = map(int, input().split())
    # 양방향 이동이 가능하므로 두 군데 모두 넣어줘야함
    graph[start].append(end)
    graph[end].append(start)
# 시작 위치까지의 거리는 0으로 설정
distance[1] = 0
h = []
# 큐에 시작 위치를 넣어줌
heapq.heappush(h, 1)
while h:
    num = heapq.heappop(h)
    # 이어져있는 통로를 모두 검사
    for i in graph[num]:
        # 이미 최솟값으로 설정이 되어있는 경우 무시하고 계속함
        if distance[i] <= distance[num] + 1:
            continue
        # 새로 검사하는 경우가 최솟값인 경우 값을 갱신해주고 큐에 현재 위치를 넣어줌
        else:
            distance[i] = distance[num] + 1
            heapq.heappush(h, i)

for i in range(1, N + 1):
    # 갈 수 없는 곳이 있는 경우 거리를 -1로 설정
    if distance[i] == INF:
        distance[i] = -1
# 시작점에서 가장 멀리 있는 헛간의 거리를 구함
far_away = max(distance[1:])
# 가장 멀리 있는 지점과 거리가 같은 헛간의 개수를 구함
cnt = distance.count(far_away)
# 숨을 헛간
hide = 0
for i in range(1, N + 1):
    # 처음으로 가장 먼 헛간이 나오는 경우 그곳을 숨는 헛간으로 정함
    if far_away == distance[i]:
        hide = i
        break
print(hide, far_away, cnt)