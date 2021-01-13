def check_correct(str):
    open = 0
    if len(str) == 0:
        return True
    for i in range(len(str)-1):
        if str[i] == '(':
            open += 1
        elif str[i] == ')':
            open -= 1
        if open < 0:
            return False
    return True

def check_balance(str):
    open = 0
    close = 0
    for i in range(len(str)):
        if str[i] == '(':
            open += 1
        elif str[i] == ')':
            close += 1
        if open == close:
            return i

def correcting(str):
    if check_correct(str):
        return str
    u_index = check_balance(str)
    u = ''
    v = ''
    if str == '':
        return ''
    else:
        u += str[:u_index+1]
        v += str[u_index+1:]
        if check_correct(u):
            str = correcting(v)
        else:
            tmp = '(' + correcting(v) + ')'
            tmp_u = ''
            for i in range(1, len(u)-1):
                if u[i] == '(':
                    tmp_u += ')'
                elif u[i] == ')':
                    tmp_u += '('
            return tmp + tmp_u
    return u + str

def solution(p):
    answer = ''
    answer = correcting(p)
    return answer

print(solution('(()())()'))
print(solution(")("))
print(solution("()))((()"))