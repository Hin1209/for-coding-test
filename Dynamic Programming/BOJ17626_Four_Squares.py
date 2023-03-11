import sys

input = sys.stdin.readline

n = int(input())

dp_table = [5 for i in range(50001)]
dp_table[0] = 0
dp_table[1] = 1
for i in range(1, 50001):
    dp_table[i] = dp_table[i-1] + dp_table[1]
    for j in range(2, 50001):
        if j * j > i:
            break
        dp_table[i] = min(dp_table[i], 1+dp_table[i-j*j])
print(dp_table[n])