import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

liquid = list(map(int, input().split()))
if n == 2:
    print(liquid[0], liquid[1])
else:
    start = 0
    end = len(liquid)
    while True:
        if start >= end:
            middle = -1
            break
        middle = (start + end) // 2
        if middle == 0:
            middle = -1
            break
        if liquid[middle] > 0:
            if liquid[middle - 1] < 0:
                break
            else:
                end = middle
        else:
            if middle == len(liquid) - 1:
                middle = -1
                break
            if liquid[middle + 1] > 0:
                middle = middle + 1
                break
            else:
                start = middle
        
    if middle == -1:
        if liquid[0] > 0:
            print(liquid[0], liquid[1])
        else:
            print(liquid[-2], liquid[-1])
    else:
        alkal = middle-1
        acid = middle 
        if alkal > 0:
            res = abs(liquid[alkal] + liquid[alkal-1])
            pair = (liquid[alkal-1], liquid[alkal])
            if acid < len(liquid) - 1:
                tmp = abs(liquid[acid] + liquid[acid+1])
                if res > tmp:
                    res = tmp
                    pair = (liquid[acid], liquid[acid+1])
        else:
            if acid == len(liquid) - 1:
                res = 1e9
            else:
                res = abs(liquid[acid] + liquid[acid+1])
                pair = (liquid[acid], liquid[acid+1])
        
        while acid < len(liquid) and alkal >= 0:
            tmp = liquid[acid] + liquid[alkal]
            if abs(tmp) < res:
                res = abs(tmp)
                pair = (liquid[alkal], liquid[acid])
            if tmp > 0:
                alkal -= 1
            else:
                acid += 1
        print(pair[0], pair[1])
        