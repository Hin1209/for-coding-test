import sys
import math
input = sys.stdin.readline

n = int(input())

dist = [[0] * n for _ in range(n)]
build = []
for i in range(n):
    x, y = map(int, input().split())
    build.append((x,y))
    
def find_dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

for i in range(n):
    for j in range(n):
        dist[i][j] = find_dist(build[i], build[j])
max_point = []
for i in range(n):
    max_point.append(max(dist[i]))
min_dist = 1e9
min_point = 0
for i in range(n):
    if max_point[i] < min_dist:
        min_point = i
        min_dist = max_point[i]
min_pos = build[min_point]
print(min_pos[0], min_pos[1])