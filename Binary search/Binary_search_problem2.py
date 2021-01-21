n = int(input())
L = list(map(int, input().split()))
start = 0
end = n - 1
result = -1

while start <= end:
    mid = (start + end) // 2
    if L[mid] == mid:
        result = mid
        break
    elif L[mid] < mid:
        start = mid + 1
    elif L[mid] > mid:
        end = mid - 1
print(result)
