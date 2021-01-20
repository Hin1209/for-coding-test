import sys
n, c = list(map(int, sys.stdin.readline().split()))
house = []
antenna = []
start = 0
end = len(house) - 1
for _ in range(n):
    house.append(int(sys.stdin.readline()))
house.sort()
min_distance = house[-1] - house[0]
antenna.append(0)
antenna.append(len(house)-1)
c -= 2


def setAntenna(house, antenna, start, end, cnt, mindistance):
    if cnt == 0:
        return True
    if start > end:
        return True
    mid = (start + end) // 2
