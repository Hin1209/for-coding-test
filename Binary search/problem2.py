import sys
def search_partial_sum(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if sum(array[:mid+1]) + array[mid] * len(array[mid+1:]) == target:
            return array[mid]
        elif sum(array[:mid+1]) + array[mid] * len(array[mid+1:]) < target:
            start = mid + 1
        elif sum(array[:mid+1]) + array[mid] * len(array[mid+1:]) > target:
            end = mid - 1
    return array[start]

n, m = list(map(int, sys.stdin.readline().split()))
have = list(map(int, sys.stdin.readline().split()))
have.sort()
loss_distance = sum(have) - m
print(search_partial_sum(have, loss_distance, 0, len(have)-1))

