# -*- coding: utf-8 -*-

def solution(N, stages):
    answer = []
    score = [0 for _ in range(N+2)] # 스코어가 n+1 까지 존재하므로 인덱스도 n+1 까지 만들어줌
    fail = [] # 실패율을 저장할 리스트
    for i in range(len(stages)):
        score[stages[i]] += 1
    for i in range(1, N+1):
        if score[i] == 0 or sum(score[i:]) == 0: # 스테이지에서 멈춘 사람이 없거나 통과한 사람이 없으면 실패율을 0으로 설정
            rate_fail = 0
        else:
            rate_fail = score[i]/sum(score[i:]) # 실패율 = 멈춘 사람/(멈춘 사람+통과한 사람)
        fail.append((i, rate_fail)) # 스테이지와 실패율을 fail에 저장
    fail.sort(key = lambda x : (-x[1], x[0])) # 실패율이 높은 순으로 정렬함.
    for i in fail:
        answer.append(i[0]) # answer에 스테이지만 저장

    return answer
print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4,4,4,4,4]))