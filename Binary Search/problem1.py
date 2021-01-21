import sys
n = int(sys.stdin.readline().rstrip())
have = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline().rstrip())
need = list(map(int, sys.stdin.readline().split()))
have.sort()
def binary_search(array, start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return True
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False
check = 0
for i in need:
    if binary_search(have, 0, len(have)-1, i):
        print("YES", end = ' ')
    else:
        print("NO", end = ' ')