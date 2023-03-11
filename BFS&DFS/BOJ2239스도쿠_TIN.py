import sys
from collections import deque

input = sys.stdin.readline

board = [[0] * 9 for _ in range(9)]
tmp = []

for _ in range(9):
    tmp.append(input().rstrip())
    
for i in range(9):
    for j in range(9):
        board[i][j] = int(tmp[i][j])

def dfs(x, y):
    if board[y][x] != 0:
        if x == 8:
            if y == 8:
                return True 
            else:
                if not dfs(0,y+1):
                    return False
                else:
                    return True
        else:
            if not dfs(x+1, y):
                return False
            else:
                return True
    else:
        posx = x // 3
        posy = y // 3
        num = {1,2,3,4,5,6,7,8,9}
        unable = set()
        for i in range(9):
            unable.add(board[i][x])
            unable.add(board[y][i])
        for i in range(3):
            for j in range(3):
                ii = i + 3 * posy
                jj = j + 3 * posx
                unable.add(board[ii][jj])
        unused = num - unable
        success = False
        if unused:
            unused = list(unused)
            unused.sort()
            for i in unused:
                board[y][x] = i
                if x == 8:
                    if y == 8:
                        return True
                    else:
                        if not dfs(0, y+1):
                            board[y][x] = 0
                        else:
                            return True
                else:
                    if not dfs(x+1, y):
                        board[y][x] = 0
                    else:
                        return True
        else:
            return False

dfs(0,0)
for i in range(9):
    for j in range(9):
        print(board[i][j], end="")
    print()