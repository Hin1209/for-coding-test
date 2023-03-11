import sys
from collections import deque
sys.setrecursionlimit(10**8)

input = sys.stdin.readline

num = int(input())

graph = [[] for _ in range(num+1)]
parents = [0] * (num+1)

for _ in range(num-1):
    parent, child, weight = map(int, input().split())
    graph[parent].append((child, weight))
    graph[child].append((parent, weight))

leafs = [len(graph[i]) == 0 for i in range(len(graph))]

max_length = 0
point = 0
visit = [0] * (num+1)

def find_far_point(node,length):
    global max_length, point
    if visit[node] == 0:
        visit[node] = 1
        if max_length < length:
            point = node
            max_length = length
        for next, weight in graph[node]:
            find_far_point(next,length+weight)
            
find_far_point(1,0)

for i in range(len(visit)):
    visit[i] = 0    
    
max_length = 0
find_far_point(point,0)

print(max_length)