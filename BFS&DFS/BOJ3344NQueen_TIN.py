import sys
from collections import deque
import heapq
sys.setrecursionlimit(10**4)

input = sys.stdin.readline

size = int(input())

table = [0 for _ in range(size)]

cnt = 0

def find_perfect(state, previous):
    if state == size:
        global cnt
        cnt += 1
    else:
        for i in range(size):
            if i == previous or i == previous-1 or i == previous+1:
                if state != 0:
                    continue
            if check_perfect(state, i):
                table[state] = i
                find_perfect(state+1,i)
                
def check_perfect(state, pos):
    for j in range(state):
        if table[j] == pos or abs(j-state) == abs(table[j]-pos):
            return False
    return True
        
find_perfect(0,0)
print(cnt)