def check_balance(s):
    unsafe = 0
    for i in range(len(s)):
        for j in range(len(s)):
            if len(s[i][j]) != 0:
                for x in s[i][j]:
                    if x == 0:
                        if i == 0:
                            continue
                        elif 1 in s[i][j] or 0 in s[i-1][j]:
                            continue
                        elif j > 0 and 1 in s[i][j-1]:
                            continue
                        else:
                            unsafe = 1
                            break
                    elif x == 1:
                        if i == 0:
                            unsafe = 1
                            break
                        elif 0 in s[i-1][j]:
                            continue
                        elif j < (len(s)-1) and 0 in s[i-1][j+1]:
                            continue
                        elif j > 0 and j < (len(s)-1) and 1 in s[i][j-1] and 1 in s[i][j+1]:
                            continue
                        else:
                            unsafe = 1
                            break
    if unsafe == 1:
        return False
    else:
        return True

def solution(n, build_frame):
    answer = []
    space = [[[] for _ in range(n+1)] for _ in range(n+1)]
    for x, y, a, b in build_frame:
        if b == 1:
            if a == 1:
                space[y][x].append(a)
                if check_balance(space):
                    continue
                else:
                    space[y][x].remove(a)
            elif a == 0:
                space[y][x].append(a)
                if check_balance(space):
                    continue
                else:
                    space[y][x].remove(a)
        elif b == 0:
            if a == 1:
                space[y][x].remove(a)
                if check_balance(space):
                    continue
                else:
                    space[y][x].append(a)
            elif a == 0:
                space[y][x].remove(a)
                if check_balance(space):
                    continue
                else:
                    space[y][x].append(a)
    for i in range(len(space)):
        for j in range(len(space)):
            if len(space[i][j]) != 0:
                for x in space[i][j]:
                    answer.append([j, i, x])
    answer.sort()

    return answer


n = 5
build_frame1 = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]
build_frame2 = [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]
print(solution(n, build_frame2))