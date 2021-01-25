import sys
import heapq

input = sys.stdin.readline
# 무한 설정
INF = int(1e9)

# 도시 개수, 통로의 개수, 시작점
n, m, c = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    s, ne, t = map(int, input().split())
    graph[s].append((ne, t))

# 거리를 저장할 테이블
distance = [INF] * (n + 1)
start = c
# 시작점까지의 거리는 0
distance[start] = 0
h = []
# 힙에 시작점의 정보 입력
heapq.heappush(h, (0, start))
while h:
    # 시작점부터 현재 위치까지의 거리, 현재 위치
    dist, now = heapq.heappop(h)
    # 시작점부터 현재 위치까지의 거리가 이미 최솟값으로 설정되어 있으면 다른 경우로 넘어감
    if distance[now] < dist:
        continue
    # i는 now에서 갈 수 있는 도시와 시간을 저장함
    for i in graph[now]:
        # 다음 도시까지의 거리는 현재 위치 + 다음 도시까지 가는 거리
        cost = dist + i[1]
        if distance[i[0]] > cost:
            distance[i[0]] = cost
            heapq.heappush(h, (cost, i[0]))

max_time = 0
cnt = 0
for i in range(1, n + 1):
    if distance[i] != INF and distance[i] != 0:
        cnt += 1
        if distance[i] > max_time:
            max_time = distance[i]
print(cnt, max_time)
