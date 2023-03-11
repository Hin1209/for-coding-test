import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

n, s = map(int, input().split())

num = list(map(int, input().split()))

front = []
back = []

def getSub(pos, end, sum, list):
    if pos == end:
        list.append(sum)
        return
    getSub(pos+1, end, sum+num[pos], list)
    getSub(pos+1, end, sum, list)

getSub(0, len(num) // 2, 0, front)
getSub(len(num) // 2, len(num), 0, back)

front.sort()
back.sort()
cnt = 0
for flag in range(len(front)):
    target = s - front[flag]
    left = bisect_left(back, target)
    right = bisect_right(back, target)
    if left != right:
        cnt += right - left
if s == 0:
    cnt -= 1
print(cnt)