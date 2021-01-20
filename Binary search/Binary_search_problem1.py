import sys
n, x = list(map(int, sys.stdin.readline().split()))
data = list(map(int, sys.stdin.readline().split()))
start = 0
end = len(data) - 1
left = 0
right = 0
left_stop = 0
right_stop = 0
while True:
    mid = (start + end) // 2
    if data[mid] == x:
        if mid == 0:
            left = mid
            left_stop = 0
        if mid == len(data) - 1:
            right = mid
            right_stop = 0
        if mid > 0 and data[mid-1] == x and left_stop == 0:
            end = mid - 1
            continue
        elif mid > 0 and data[mid-1] < x and left_stop == 0:
            left = mid
            left_stop = 1
            continue
        if mid < len(data) - 1 and data[mid+1] == x and right_stop == 0:
            start = mid + 1
            continue
        elif mid < len(data) - 1 and data[mid+1] > x and right_stop == 0:
            right = mid
            right_stop = 1
            continue
    elif data[mid] < x:
        start = mid + 1
    elif data[mid] > x:
        end = mid - 1
    if right_stop == 1 and left_stop == 1:
        break
print(right - left + 1)
