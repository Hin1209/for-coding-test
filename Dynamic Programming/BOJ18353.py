n = int(input())
soldier = list(map(int, input().split()))
dp_table = [1 for _ in range(n)]
for i in range(1, n):
    for j in range(i):
        if soldier[j] > soldier[i]:
            dp_table[i] = max(dp_table[i], dp_table[j] + 1)
print(n - max(dp_table))


# 가장 긴 증가하는 부분 수열 알고리즘(LIS)
# soldier.reverse()
# for i in range(1, n):
#     for j in range(i):
#         if soldier[j] < soldier[i]:
#             dp_table[i] = max(dp_table[i], dp_table[j] + 1)
# print(n - max(dp_table))