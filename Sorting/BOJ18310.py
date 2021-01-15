import sys
n = int(sys.stdin.readline())
house = list(map(int, sys.stdin.readline().split()))
min_distance = sum(house)
min_pos = 0
for i in range(len(house)):
    tmp_sum = 0
    for j in range(len(house)):
        tmp_sum += abs(house[i] - house[j])
    if min_distance > tmp_sum:
        min_distance = tmp_sum
        min_pos = house[i]
    if min_distance == tmp_sum:
        if min_pos == house[i]:
            continue
        else:
            break

print(min_pos)


