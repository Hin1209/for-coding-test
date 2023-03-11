import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
for i in range(n-1):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
root = 1
visited = [False] * (n+1)
h = [root]
new_graph = [[] for _ in range(n+1)]
visited[root] = True
dp = [[-1,-1] for _ in range(n+1)]
while h:
    now = h.pop()
    for next in graph[now]:
        if not visited[next]:
            visited[next] = True
            new_graph[now].append(next)
            h.append(next)

def find_min(root, early):
    if not new_graph[root]:
        if early: return 1
        else: return 0
    if dp[root][early] != -1: return dp[root][early]
    
    if early:
        dp[root][early] = 1
        for child in new_graph[root]:
            dp[root][early] += min(find_min(child, 0), find_min(child, 1))
    else:
        dp[root][early] = 0
        for child in new_graph[root]:
            dp[root][early] += find_min(child, 1)
    return dp[root][early]
graph = []
visited = []
print(min(find_min(root, 1), find_min(root, 0)))