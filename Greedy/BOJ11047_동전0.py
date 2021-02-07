import sys

input = sys.stdin.readline

N, K = map(int, input().split())

coin = []

for _ in range(N):
    c = int(input())
    coin.append(c)

if K in coin:
    print(1)
else:
    check_index = len(coin) - 1
    target = K
    min_coin = 0

    while target != 0:
        if target // coin[check_index] != 0:
            min_coin += target // coin[check_index]
            target %= coin[check_index]
        check_index -= 1

    print(min_coin)
