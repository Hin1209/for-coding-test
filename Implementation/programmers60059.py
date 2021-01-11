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
            answer = True # 조건을 만족하는 경우 answer를 True로 설정하고 반복문 탈출
            break
        if(len(p_lock) > len(p_key)): # 홈이 열쇠의 돌기보다 많으면 열 수 없음
            answer = False # 조건을 만족하는 경우 answer를 False로 설정하고 반복문 탈출
            break
        else:
            for i in range(-len(lock), len(lock)+1): # 여기서 i는 평행이동을 위한 변수. 움직일 수 있는 최대 범위가 상하좌우로 자물쇠의 크기만큼임
                if (count == len(p_lock) and stop == 1): # 열쇠의 돌기와 자물쇠의 홈이 일치하는 수가 자물쇠의 모든 홈의 개수와 같아짐.
                    break # 아래에 있는 똑같은 if문은 아래 j를 변수로 하는 for문을 탈출하기 위한 조건문
                for j in range(-len(lock), len(lock)+1): # j도 평행이동을 위한 변수
                    count = 0 # 평행이동을 할 때마다 count를 새로 세어줌
                    tmp = [] # tmp는 평행이동을 하고 난 후 열쇠의 돌기 위치를 저장하기 위한 리스트임
                    for k in p_key: # k에 현재 열쇠 돌기의 위치를 대입
                        tmp.append((k[0]+i, k[1]+j)) # tmp에 k를 (i, j) 만큼 평행이동한 값을 저장함
                    for z in p_lock: # z에 자물쇠 홈 위치를 대입
                        if z in tmp: # 자물쇠 홈 위치가 평행이동 시킨 열쇠의 돌기 위치와 일치하면 count를 1 늘려줌
                            count += 1
                        else:
                            answer = False # 자물쇠의 홈이 하나라도 남으면 열 수 없으므로 answer를 False로 설정
                    if(count == len(p_lock)): # count가 자물쇠의 홈 개수와 일치
                        for le in tmp: # 평행이동한 열쇠의 돌기 중에 자물쇠의 돌기와 닿는 부분이 있는지 확인
                            if 0 <= le[0] < len(lock) and 0 <= le[1] < len(lock): # 자물쇠 범위 밖은 신경쓰지 않아도 됨
                                if(lock[le[0]][le[1]] == 1): # 열쇠의 돌기 중 자물쇠의 돌기와 닿는 부분이 있으면 자물쇠를 열 수 없음
                                    answer = False
                                    stop = 0 # 반복문을 멈추지 않기 위해 stop을 0으로 설정하고 반복문 탈출
                                    break
                            stop = 1 # 위의 조건에 걸리지 않으면 자물쇠를 열 수 있는 것이므로 stop을 1로 설정해 반복문을 끝냄
                        if(stop == 1): # 이 조건문은 for j 문을 탈출하기 위한 조건문임
                            answer = True
                            break
        if(answer == True): # 위의 for문 안의 break가 for문만 탈출할 수 있기 때문에 while문 탈출을 위한 조건을 추가
            break
        key = turn_array(key) # 경우를 반복했을 때 자물쇠가 열리지 않으면 키를 회전시킴
        r += 1 # 회전시킨 수 증가
    return answer