# -*- coding: utf-8 -*-

import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    array = list(map(int, sys.stdin.readline().split()))
    tmp_level = 0
    reverse_index = 0
    array.sort()
    level = array[n-1] - array[0]

    for i in range(1, n):
        tmp_level = max(abs(array[i] - array[0]), abs(array[n-1] - array[i-1]))
        if(tmp_level < level):
            level = tmp_level
            reverse_index = i
    partial = array[reverse_index:]
    partial.sort(reverse=True)
    print(array)
    print(partial)
    print(level)








    # for i in range(n):
    #     for j in range(n):
    #         if(i == n-1):
    #             right_min_level = abs(array[n-1] - array[0])
    #         else:
    #             right_min_level = abs(array[i+1] - array[i])
    #         if(i == 0):
    #             left_min_level = abs(array[n-1] - array[0])
    #         else:
    #             left_min_level = abs(array[i] - array[i-1])
    #         if(i == j):
    #             continue
    #         elif(i == 0):
    #             if(abs(array[j] - array[i]) < right_min_level):
    #                 right_min_level = abs(array[j] - array[i])
    #                 tmp = array[i+1]
    #                 array[i+1] = array[j]
    #                 array[j] = tmp
    #             if (j != i+1 and abs(array[j] - array[0]) < left_min_level):
    #                 left_min_level = abs(array[j] - array[0])
    #                 tmp = array[n-1]
    #                 array[n-1] = array[j]
    #                 array[j] = tmp
    #         elif(i == n-1):
    #             if (abs(array[j] - array[n-1]) < right_min_level):
    #                 min_level = abs(array[j] - array[n-1])
    #                 tmp = array[0]
    #                 array[0] = array[j]
    #                 array[j] = tmp
    #             if (j != i+1 and abs(array[j] - array[i]) < left_min_level):
    #                 min_level = abs(array[j] - array[i])
    #                 tmp = array[i - 1]
    #                 array[i - 1] = array[j]
    #                 array[j] = tmp
    #         else:
    #             if (abs(array[j] - array[i]) < right_min_level):
    #                 min_level = abs(array[j] - array[i])
    #                 tmp = array[i + 1]
    #                 array[i + 1] = array[j]
    #                 array[j] = tmp
    #             if (j != i+1 and abs(array[j] - array[i]) < left_min_level):
    #                 min_level = abs(array[j] - array[i])
    #                 tmp = array[i - 1]
    #                 array[i - 1] = array[j]
    #                 array[j] = tmp
    # for i in range(n):
    #     if(i == 0):
    #         if (abs(array[0] - array[n-1]) > level):
    #             level = abs(array[0] - array[n-1])
    #     else:
    #         if(abs(array[i] - array[i-1]) > level):
    #             level = abs(array[i] - array[i+1])