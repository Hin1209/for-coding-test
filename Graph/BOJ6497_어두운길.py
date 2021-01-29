import sys

input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_group(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

while True:
    N, M = map(int, input().split())
    # 마지막 입력 0 0이 나오면 종료
    if N == 0 and M == 0:
        break
    # 길들의 정보와 비용을 저장할 리스트
    edge = []
    parent = [0] * N

    for i in range(N):
        parent[i] = i
    # 모든 길의 비용의 총합
    original_cost = 0

    for _ in range(M):
        a, b, c = map(int, input().split())
        edge.append((c, a, b))
        original_cost += c
    # 길들을 비용 순으로 정렬
    edge.sort()
    # 길을 최소한만 남겼을때의 비용
    sum_load = 0
    # 최소 스패닝 트리
    for i in edge:
        cost, a, b = i
        if find_parent(parent, a) != find_parent(parent, b):
            union_group(parent, a, b)
            sum_load += cost

    # 원래 비용과 최소 비용의 차이를 출력
    print(original_cost - sum_load)
