import sys
from collections import deque
sys.setrecursionlimit(10**8)

input = sys.stdin.readline

num = int(input())

graph = [[] for _ in range(num+1)]

for _ in range(num):
    tmp = list(map(int, input().split()))
    for i in range(1,len(tmp),2):
        if tmp[i] == -1:
            break
        graph[tmp[0]].append((tmp[i],tmp[i+1]))

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