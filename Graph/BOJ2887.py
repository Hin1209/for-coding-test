import sys

input = sys.stdin.readline
INF = int(1e9)

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

N = int(input())
# 행성들의 x, y, z 좌표를 저장함
pos_planet_x = []
pos_planet_y = []
pos_planet_z = []
# 행성간 터널과 비용을 저장함
cost_tunnel = []
# 행성들이 속한 집합
parent = [0] * N
# 처음에는 각자 다른 집합에 속해있음
for i in range(N):
    parent[i] = i

# 행성의 좌표 입력
for i in range(N):
    x, y, z = map(int, input().split())
    pos_planet_x.append((x, i))
    pos_planet_y.append((y, i))
    pos_planet_z.append((z, i))
# 입력받은 좌표를 크기순으로 정렬함
pos_planet_x.sort()
pos_planet_y.sort()
pos_planet_z.sort()
# 서로 인접한 행성들끼리의 터널만 cost_tunnel에 저장함
for i in range(N - 1):
    dx = pos_planet_x[i + 1][0] - pos_planet_x[i][0]
    dy = pos_planet_y[i + 1][0] - pos_planet_y[i][0]
    dz = pos_planet_z[i + 1][0] - pos_planet_z[i][0]
    cost_tunnel.append((dx, pos_planet_x[i][1], pos_planet_x[i + 1][1]))
    cost_tunnel.append((dy, pos_planet_y[i][1], pos_planet_y[i + 1][1]))
    cost_tunnel.append((dz, pos_planet_z[i][1], pos_planet_z[i + 1][1]))

# 터널의 비용순으로 정렬
cost_tunnel.sort()
min_cost = 0

# 비용이 적게 드는 터널부터 차례대로 터널을 이어줌
for i in cost_tunnel:
    c, a, b = i
    if find_parent(parent, a) != find_parent(parent, b):
        union_group(parent, a, b)
        min_cost += c

print(min_cost)