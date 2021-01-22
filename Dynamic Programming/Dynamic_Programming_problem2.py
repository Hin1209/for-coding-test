n = int(input())
dp_table = [0] * n
dp_table[0] = 1
# 2배, 3배, 5배를 위한 인덱스
i2 = i3 = i5 = 0
# 처음 곱셈 해줄 값을 초기화 시킴
next2, next3, next5 = 2, 3, 5

for i in range(1, n):
    dp_table[i] = min(next2, next3, next5)

    if dp_table[i] == next2:
        i2 += 1
        next2 = dp_table[i2] * 2
    if dp_table[i] == next3:
        i3 += 1
        next3 = dp_table[i3] * 3
    if dp_table[i] == next5:
        i5 += 1
        next5 = dp_table[i5] * 5
print(dp_table[n-1])

