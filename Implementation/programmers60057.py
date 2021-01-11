# -*- coding: utf-8 -*-

def solution(s):
    answer = 0
    can = [] # 가능한 문자열의 길이를 저장하는 리스트
    count = 1 # 반복되는 구간의 갯수를 임시로 저장할 변수. 구간이 최소 하나는 있으므로 1부터 시작
    for i in range(1, len(s)+1): # i는 구간의 길이
        flag = 0 # 구간의 시작점. 처음에는 0에서 시작
        result = '' # 압축한 결과

        for j in range(len(s) // i): # flag가 인덱스 값을 벗어나지 않게 하기 위해 구간의 길이 i로 나눈 몫까지만 진행
            nflag = flag+i # 다음 구간의 시작 인덱스
            if(s[flag:flag+i] == s[nflag:nflag+i]): # 현재 도는 구간과 다음 구간이 같은지 확인
                count += 1 # 다음 구간과 일치하면 개수를 늘려줌
            else:
                if(count == 1): # 다음 구간과 불일치 하는데 지금까지 같은 구간이 하나도 없을 경우.
                    result += s[flag:flag+i] # 이 때는 숫자는 생략하고 구간 문자열만 추가
                else:
                    result += str(count) + s[flag:flag+i] # 반복 구간이 여러개라면 반복된 횟수도 추가
                count = 1 # 개수를 다시 세기 위해 1로 초기화
            flag += i # 다음 구간으로 넘어가기 위해 구간 길이인 i 만큼 이동함
            if(nflag < len(s) and nflag+i > len(s)): # 비교할 구간의 시작점은 리스트 안인데, 끝나는 점이 범위 초과일때는 그 구간을 그대로 넣어줌.
                result += s[nflag:]
                break

        can.append(len(result)) # can 리스트에 압축된 문자열의 길이를 추가함.
    answer = min(can) # 문자열의 길이를 담고 있는 can 에서 최솟값이 우리가 찾는 정답.
    return answer

