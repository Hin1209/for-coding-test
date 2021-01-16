def solution(N, stages):
    answer = []
    score = [0 for _ in range(N+2)]
    fail = []
    for i in range(len(stages)):
        score[stages[i]] += 1
    for i in range(1, N+1):
        if score[i] == 0 or sum(score[i:]) == 0:
            rate_fail = 0
        else:
            rate_fail = score[i]/sum(score[i:])
        fail.append((i, rate_fail))
    fail.sort(key = lambda x : (-x[1], x[0]))
    for i in fail:
        answer.append(i[0])

    return answer
print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4,4,4,4,4]))