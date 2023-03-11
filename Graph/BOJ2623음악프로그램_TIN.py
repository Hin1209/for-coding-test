import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
inorder = [0] * (n+1)
inorder[0] = -1
for i in range(m):
    tmp_order = list(map(int, input().split()))
    for j in range(2,len(tmp_order)):
        graph[tmp_order[j-1]].append(tmp_order[j])
        inorder[tmp_order[j]] += 1

deq = deque()
res = []
for i in range(1,n+1):
    if inorder[i] == 0:
        deq.append(i)

while deq:
    now = deq.popleft()
    res.append(now)
    for next in graph[now]:
        inorder[next] -= 1
        if inorder[next] == 0:
            deq.append(next)

if len(res) != n:
    print(0)
else:
    for i in res:
        print(i) 