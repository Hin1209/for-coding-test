def check_correct(str): # 올바른 괄호인지 체크
    open = 0
    if len(str) == 0:
        return True
    for i in range(len(str)-1):
        if str[i] == '(':
            open += 1
        elif str[i] == ')':
            open -= 1
        if open < 0: # ) 가 ( 보다 많이 나오면 올바르지 않음.
            return False
    return True

def check_balance(str): # 균형잡힌 괄호인지 체크
    open = 0
    close = 0
    for i in range(len(str)):
        if str[i] == '(':
            open += 1
        elif str[i] == ')':
            close += 1
        if open == close: # 왼쪽 괄호와 오른쪽 괄호의 개수가 같으면 균형잡힌 괄호이고 그 인덱스를 반환
            return i

def correcting(str):
    if check_correct(str): # 올바른 괄호면 그대로 리턴
        return str
    u_index = check_balance(str) # 균형잡힌 괄호 문자열의 마지막 인덱스
    u = ''
    v = ''
    if str == '': # 빈 문자열이면 그대로 리턴
        return ''
    else:
        u += str[:u_index+1] # 균형잡힌 괄호 문자열
        v += str[u_index+1:] # 나머지 문자열
        if check_correct(u): # 올바른 문자열이면 나머지 문자열 v에 대해서 다시 correcting함.
            str = correcting(v)
        else: # u가 올바른 문자열이 아닐 경우
            tmp = '(' + correcting(v) + ')' # v를 correcting 하고 앞뒤에 ()를 붙임.
            tmp_u = ''
            for i in range(1, len(u)-1): # u의 양 끝 괄호 제거
                if u[i] == '(': # 나머지 괄호를 뒤집어서 추가해줌
                    tmp_u += ')'
                elif u[i] == ')':
                    tmp_u += '('
            return tmp + tmp_u # 뒤집은 u를 뒤에 붙여줌
    return u + str # 마지막에는 u에 수정된 str을 붙여줌

def solution(p):
    answer = ''
    answer = correcting(p)
    return answer

print(solution('(()())()'))
print(solution(")("))
print(solution("()))((()"))