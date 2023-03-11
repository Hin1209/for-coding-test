import sys
from collections import deque
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

red = 1
blue = -1

def bfs(x, color, nodes, graph):
    deq = deque()
    deq.append((x, color))
    
    while deq:
        node, col = deq.popleft()
        for next in graph[node]:
            if nodes[next] == 0:
                deq.append((next, col * -1))
                nodes[next] = col * -1
            elif nodes[next] == col:
                return False
    return True

k = int(input())

for _ in range(k):
    v, e = map(int, input().split())
    
    nodes = [0] * (v + 1)
    graph = [[] for _ in range(v + 1)]
    
    for i in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    bigraph = True
        
    for i in range(1, v + 1):
        if nodes[i] == 0:
            if not bfs(i, red, nodes, graph):
                bigraph = False
                break
            
    if bigraph:
        print("YES")
    else:
        print("NO")