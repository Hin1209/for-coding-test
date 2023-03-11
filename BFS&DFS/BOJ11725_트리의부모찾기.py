import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

def find_parent(x):
    if node[x]:
        for next in node[x]:
            if parent[next] == -1:
                parent[next] = x
                find_parent(next)


n = int(input())

parent = [-1] * (n + 1)

parent[1] = 1

node = [[] for _ in range(n + 1)]

for i in range(n - 1):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

find_parent(1)

for i in range(2, n + 1):
    print(parent[i])

