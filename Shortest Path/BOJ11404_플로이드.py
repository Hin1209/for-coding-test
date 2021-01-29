import sys

input = sys.stdin.readline
# 무한 설정
INF = int(1e9)

n = int(input())
m = int(input())
# 2차원 리스트 생성
graph = [[INF for _ in range(n + 1)] for _ in range(n + 1)]

for _ in range(m):
    start, next, time = map(int, input().split())
    # 도시간의 통로가 하나가 아닌 경우도 있으므로 통로중에 거리가 가장 짧은 통로를 고름
    graph[start][next] = min(time, graph[start][next])

for i in range(1, n + 1):
    # 이동하지 않는 경우 거리가 0
    graph[i][i] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # 다른 도시를 거쳐 오는 경우와 현재 저장된 거리 중 작은 것을 선택
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        # 이동이 불가능한 도시는 0으로 설정해줌
        if graph[i][j] == INF:
            graph[i][j] = 0
        print(graph[i][j], end = ' ')
    print()

