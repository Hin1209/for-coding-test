n = int(input())
chart = []
dp_table = [0 for _ in range(n+1)]
for _ in range(n):
    chart.append(tuple(map(int, input().split())))

for i in range(n):
    if i + chart[i][0] <= n:
        for j in range(i + chart[i][0], n+1):
            dp_table[j] = max(dp_table[j], dp_table[i] + chart[i][1])
print(max(dp_table))
