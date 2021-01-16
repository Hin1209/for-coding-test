import sys
n = int(sys.stdin.readline())
house = list(map(int, sys.stdin.readline().split()))
total_sum = sum(house)
house.sort()
if n % 2 == 0:
    print(house[len(house)//2 - 1])
else:
    print(house[len(house)//2])
