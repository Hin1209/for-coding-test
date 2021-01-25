import sys

# 무한 설정
INF = int(1e9)
input = sys.stdin.readline

N, m = map(int, input().split())
# 2차원 리스트 생성 (행이 출발, 열이 도착)
graph = [[INF] * (N + 1) for _ in range(N + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    # 양방향 통행 가능
    graph[a][b] = 1
    graph[b][a] = 1
x, k = map(int, input().split())
for a in range(1, N + 1):
    for b in range(1, N + 1):
        if a == b:
            # 출발 지점과 도착 지점이 같으면 걸리는 시간 0
            graph[a][b] = 0

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            # i에서 j로 가는 시간과 i에서 k를 거쳐 j로 가는 것 중 시간이 덜 걸리는 경우를 선택
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 시작점에서 k를 들러 x로 가는 길이 존재하지 않으면 -1 출력
if graph[1][k] >= INF or graph[k][x] >= INF:
    print(-1)
# 가능한 경우 걸리는 총 시간 출력
else:
    print(graph[1][k] + graph[k][x])
