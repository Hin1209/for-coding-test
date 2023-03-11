import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())

inorder = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    first, second = map(int, input().split())
    graph[first].append(second)
    inorder[second] += 1

h = []

for i in range(1, n+1):
    if inorder[i] == 0:
        heapq.heappush(h, i)
res = []
while h:
    now = heapq.heappop(h)
    res.append(now)
    for next in graph[now]:
        inorder[next] -= 1
        if inorder[next] == 0:
            heapq.heappush(h, next)
for i in res:
    print(i, end = " ")