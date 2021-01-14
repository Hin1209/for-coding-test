import copy
import sys
sys.setrecursionlimit(10**6)

n = int(input())
space = [['X' for _ in range(n)] for _ in range(n)]
for i in range(n):
    a = input()
    for j in range(n):
        space[i][j] = a[j]
blue = 0
red = 0
green = 0
normal = 0
blind = 0
normal_visited = [[0 for _ in range(n)] for _ in range(n)]
blind_visited = [[0 for _ in range(n)] for _ in range(n)]

def dfs(y, x, color, visited, sp, blind):
    if blind == 0:
        visited[y][x] = 1
        sp[y][x] = 0
        if y > 0:
            if sp[y-1][x] == color and visited[y-1][x] == 0:
                dfs(y-1, x, color, visited, sp, 0)
        if y < len(sp)-1:
            if sp[y+1][x] == color and visited[y+1][x] == 0:
                dfs(y+1, x, color, visited, sp, 0)
        if x > 0:
            if sp[y][x-1] == color and visited[y][x-1] == 0:
                dfs(y, x-1, color, visited, sp, 0)
        if x < len(sp)-1:
            if sp[y][x+1] == color and visited[y][x+1] == 0:
                dfs(y, x+1, color, visited, sp, 0)
    else:
        if color == 'R' or color == 'G':
            visited[y][x] = 1
            sp[y][x] = 0
            if y > 0:
                if sp[y - 1][x] == 'R' and visited[y - 1][x] == 0:
                    dfs(y - 1, x, color, visited, sp, 1)
                elif sp[y - 1][x] == 'G' and visited[y - 1][x] == 0:
                    dfs(y - 1, x, color, visited, sp, 1)
            if y < len(sp) - 1:
                if sp[y + 1][x] == 'R' and visited[y + 1][x] == 0:
                    dfs(y + 1, x, color, visited, sp, 1)
                elif sp[y + 1][x] == 'G' and visited[y + 1][x] == 0:
                    dfs(y + 1, x, color, visited, sp, 1)
            if x > 0:
                if sp[y][x - 1] == 'R' and visited[y][x - 1] == 0:
                    dfs(y, x - 1, color, visited, sp, 1)
                elif sp[y][x - 1] == 'G' and visited[y][x - 1] == 0:
                    dfs(y, x - 1, color, visited, sp, 1)
            if x < len(sp) - 1:
                if sp[y][x + 1] == 'R' and visited[y][x + 1] == 0:
                    dfs(y, x + 1, color, visited, sp, 1)
                elif sp[y][x + 1] == 'G' and visited[y][x + 1] == 0:
                    dfs(y, x + 1, color, visited, sp, 1)
        else:
            visited[y][x] = 1
            sp[y][x] = 0
            if y > 0:
                if sp[y - 1][x] == color and visited[y - 1][x] == 0:
                    dfs(y - 1, x, color, visited, sp, 1)
            if y < len(sp) - 1:
                if sp[y + 1][x] == color and visited[y + 1][x] == 0:
                    dfs(y + 1, x, color, visited, sp, 1)
            if x > 0:
                if sp[y][x - 1] == color and visited[y][x - 1] == 0:
                    dfs(y, x - 1, color, visited, sp, 1)
            if x < len(sp) - 1:
                if sp[y][x + 1] == color and visited[y][x + 1] == 0:
                    dfs(y, x + 1, color, visited, sp, 1)

tmp = copy.deepcopy(space)
for i in range(n):
    for j in range(n):
        if tmp[i][j] == 'B':
            dfs(i, j, 'B', normal_visited, tmp, 0)
            blue += 1
        elif tmp[i][j] == 'R':
            dfs(i, j, 'R', normal_visited, tmp, 0)
            red += 1
        elif tmp[i][j] == 'G':
            dfs(i, j, 'G', normal_visited, tmp, 0)
            green += 1
normal = blue + red + green
blue = 0
red = 0
tmp = copy.deepcopy(space)

for i in range(n):
    for j in range(n):
        if tmp[i][j] == 'B':
            dfs(i, j, 'B', blind_visited, tmp, 1)
            blue += 1
        elif tmp[i][j] == 'R' or tmp[i][j] == 'G':
            dfs(i, j, 'R', blind_visited, tmp, 1)
            red += 1
blind = blue + red
print(normal, blind)


