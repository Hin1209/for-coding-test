n = int(input())
warehouse = list(map(int, input().split()))
max_food = [0] * n
max_food[0] = warehouse[0]
max_food[1] = warehouse[1]
for i in range(2, n):
    if max_food[i] == 0:
        max_food[i] = warehouse[i] + max(max_food[:i-1])
print(max(max_food))
