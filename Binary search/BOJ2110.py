import sys
n, c = list(map(int, sys.stdin.readline().split()))
house = []
for _ in range(n):
    house.append(int(sys.stdin.readline()))
house.sort()
# minInterval = house[1] - house[0] -> minInterval이 항상 house[1] - house[0]이 아닐 수도 있음.
minInterval = house[-1] - house[0]
for i in range(1, n):
    if house[i] - house[i-1] < minInterval:
        minInterval = house[i] - house[i-1]
maxInterval = house[-1] - house[0]
result = 0

while minInterval <= maxInterval:
    midInterval = (minInterval + maxInterval) // 2
    # 안테나를 설치할 위치
    pos_antenna = house[0]
    # 설치한 안테나의 개수
    count = 1
    for i in range(1, n):
        # 설정한 간격보다 멀리 있는 집에 안테나 설치
        if house[i] >= pos_antenna + midInterval:
            pos_antenna = house[i]
            count += 1
    # 설치한 안테나의 개수가 문제에서 요구한 안테나의 개수보다 많거나 같으면 간격을 더 늘려서 설치해봄
    if count >= c:
        minInterval = midInterval + 1
        result = midInterval
    # 설치한 안테나의 개수가 문제에서 요구한 안테나의 개수보다 작으면 간격을 좁혀서 설치해봄
    else:
        maxInterval = midInterval - 1
print(result)

