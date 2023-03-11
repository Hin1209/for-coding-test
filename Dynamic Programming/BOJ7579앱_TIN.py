import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int, input().split())

memory = list(map(int, input().split()))
cost = list(map(int, input().split()))

app = []
for i in range(n):
    app.append((memory[i], cost[i]))
    
app.sort()
costs = [0] * (10001)
for j in range(len(app)):
    memory, cost = app[j]
    for i in reversed(range(len(costs))):
        if i >= cost:
            costs[i] = max(costs[i], costs[i-cost] + memory)
    
result = []        
for i in range(len(costs)):
    if costs[i] >= m:
        result.append((costs[i], i))
result.sort()
print(result[0][1])
    
