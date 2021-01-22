n = int(input())
dp_table = [0 for _ in range(100000001)]
dp_table[1] = 1
cnt = 0
for i in range(len(dp_table)):
    if dp_table[i] == 1:
        if i * 2 >= len(dp_table):
            break
        dp_table[i * 2] = 1
        if i * 3 >= len(dp_table):
            continue
        dp_table[i * 3] = 1
        if i * 5 >= len(dp_table):
            continue
        dp_table[i * 5] = 1
for i in range(1, len(dp_table)):
    if dp_table[i] == 1:
        cnt += 1
    if cnt == n:
        print(i)
        break

