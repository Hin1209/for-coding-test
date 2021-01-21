import sys

# 왼쪽 끝 인덱스를 찾는 함수
def search_left(array, start, end, target):
    if start > end:
        return None
    mid = (start + end) // 2
    if (mid == 0 or array[mid-1] < target) and array[mid] == target:
        return mid
    elif array[mid] < target:
        return search_left(array, mid + 1, end, target)
    elif array[mid] > target:
        return search_left(array, start, mid - 1, target)

# 오른쪽 끝 인덱스를 찾는 함수
def search_right(array, start, end, target):
    if start > end:
        return None
    mid = (start + end) // 2
    if (mid == len(array)-1 or array[mid + 1] > target) and array[mid] == target:
        return mid
    elif array[mid] < target:
        return search_right(array, mid + 1, end, target)
    elif array[mid] > target:
        return search_right(array, start, mid - 1, target)


n, x = list(map(int, sys.stdin.readline().split()))
data = list(map(int, sys.stdin.readline().split()))
start = 0
end = len(data) - 1
left = search_left(data, start, end, x)
right = search_right(data, start, end, x)

print(right - left + 1)
