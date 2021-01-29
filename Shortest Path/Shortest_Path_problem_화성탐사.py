import sys
from collections import deque

input = sys.stdin.readline
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

T = int(input())
for _ in range(T):
    N = int(input())
    visited = [[0 for _ in range(N)] for _ in range(N)]
    # 각각의 위치에서 드는 비용
    board = []
    # 각각의 위치까지 갔을 때 드는 최소 비용
    cost_map = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        board.append(list(map(int, input().split())))
    cost_map[0][0] = board[0][0]
    q = deque()
    # 큐에 시작 위치를 저장해줌
    q.append([0, 0, cost_map[0][0]])
    # 시작 위치 방문 처리
    visited[0][0] = 1
    while q:
        y, x, cost = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nx < N and 0 <= ny < N:
                # 아직 방문한 적이 없다면 최소 비용을 초기화 시켜줌
                if visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    cost_map[ny][nx] = board[ny][nx] + cost
                    q.append([ny, nx, cost_map[ny][nx]])
                # 방문한 적이 있는 경우 현재 저장된 최소 비용과 비교하여 최솟값을 선택함
                else:
                    if cost_map[ny][nx] > cost + board[ny][nx]:
                        cost_map[ny][nx] = cost + board[ny][nx]
                        q.append([ny, nx, cost_map[ny][nx]])
    # 이동이 끝난 후 모서리에 갔을때 최소 비용 출력
    print(cost_map[N-1][N-1])

