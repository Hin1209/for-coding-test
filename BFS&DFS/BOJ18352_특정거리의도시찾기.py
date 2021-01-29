from collections import deque
import sys
n, m, k, x = list(map(int, sys.stdin.readline().split()))
graph = [[] for _ in range(n+1)]
# 방문하지 않은 도시는 -1로 설정
visited = [-1 for _ in range(n+1)]
# 처음 도시는 0으로 설정
visited[x] = 0
for _ in range(m):
    # index는 출발 도시, next는 도착 도시
    index, next = list(map(int, sys.stdin.readline().split()))
    graph[index].append(next)

q = deque()
# 처음 출발하는 도시인 x를 추가
q.append(x)
result = []
while q:
    v = q.popleft()
    for nx in graph[v]:
        # 연결된 도시가 아직 방문하지 않은 도시이면 q에 추가하고 visited에 방문한 시간을 저장함
        if visited[nx] == -1:
            q.append(nx)
            visited[nx] = visited[v] + 1
check = False
for i in range(len(visited)):
    # 도시 x로부터 거리가 k인 도시를 출력함
    if visited[i] == k:
        print(i)
        check = True
if not check:
    print(-1)



