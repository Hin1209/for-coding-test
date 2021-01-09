def turn_array(ar): # 배열을 시계방향으로 회전시키는 함수
    re = [[] for i in range(len(ar))]
    for i in range(len(ar)):
        for j in range(len(ar)):
            re[i].append(ar[len(ar)-j-1][i])
    return re

def solution(key, lock):
    answer = True
    r = 0 # 회전을 한 횟수를 저장하는 변수
    count = 0 # 자물쇠의 홈과 열쇠의 돌기가 일치하는 칸의 개수
    stop = 0 # 반복문을 계속 진행할건지 아니면 멈출건지를 결정해주는 변수
    while r != 4: # 회전을 세번하고 끝날때까지 조건 만족 못하면 멈추기
        p_lock = [] # 자물쇠 홈의 위치를 저장하는 리스트
        p_key = [] # 열쇠 돌기의 위치를 저장하는 리스트
        for i in range(len(lock)):
            for j in range(len(lock)):
                if(lock[i][j] == 0): # 홈의 위치를 저장
                    p_lock.append((i, j))
        for i in range(len(key)):
            for j in range(len(key)):
                if(key[i][j] == 1): # 돌기의 위치를 저장
                    p_key.append((i, j))
        if(len(p_lock) == 0): # 홈이 하나도 없으면 열쇠가 없어도 열림
            answer = True
            break
        if(len(p_lock) > len(p_key)): # 홈이 열쇠의 돌기보다 많으면 열 수 없음
            answer = False
            break
        else:
            for i in range(-max(len(lock), len(key)), max(len(lock), len(key))+1):
                if (count == len(p_lock) and stop == 1):
                    break
                for j in range(-max(len(lock), len(key)), max(len(lock), len(key))+1):
                    count = 0
                    tmp = []
                    for k in p_key:
                        tmp.append((k[0]+i, k[1]+j))
                    for z in p_lock:
                        if z in tmp:
                            count += 1
                        else:
                            answer = False
                    if(count == len(p_lock)):
                        for le in tmp:
                            if 0 <= le[0] < len(lock) and 0 <= le[1] < len(lock):
                                if(lock[le[0]][le[1]] == 1):
                                    answer = False
                                    stop = 0
                                    break
                            stop = 1
                        if(stop == 1):
                            answer = True
                            break
        if(answer == True):
            break
        key = turn_array(key)
        r += 1
    return answer