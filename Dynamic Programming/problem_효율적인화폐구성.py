n, m = list(map(int, input().split()))
d = [0] * 10001
money = [0] * n

for i in range(n):
    money[i] = int(input())
    d[money[i]] = 1

for i in range(1, m + 1):
    if d[i] == 0:
        continue
    else:
        for j in range(n):
            if i + money[j] < m + 1:
                if d[i + money[j]] == 0:
                    d[i + money[j]] = d[i] + 1
                else:
                    d[i + money[j]] = min(d[i + money[j]], d[i] + 1)
            else:
                break
if d[m] == 0:
    print(-1)
else:
    print(d[m])


