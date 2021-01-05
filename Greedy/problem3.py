#1이 될 때까지
n, k = map(int, input().split())
cnt = 0
#반복문을 돌며 1씩 빼는것보다 1을 한번에 빼주는것이 k값이 커졌을때 더욱 효과적임
while(True):
    if(n % k == 0):
        n /= k
    else:
        n -= 1
    cnt += 1
    if(n == 1):
        break
print(cnt)


# result = 0
# while(True):
#     target = (n//k) * k
#     result += (n - target)
#     n = target
#     if(n < k):
#         break
#     result += 1
#     n //= k
#result += (n-1)
#print(result)

#답지 코드

