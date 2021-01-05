#곱하기 혹은 더하기
import time

n = input()
start = time.time()
#숫자 연산을 위해서 int로 변환
result = int(n[0])
for i in range(1, len(n)):
    #더한 값과 곱한 값을 구해주고 둘 중에 큰값을 result에 덮어씌워줌
    plus = result + int(n[i])
    mul = result * int(n[i])
    result = max(plus, mul)
print(result)
end = time.time()
print(end-start)

#더하거나 곱하는 값이 0이거나 1인 경우를 제외하면 항상 곱하는게 큰 것을 이용해 max 함수를 쓰지 않고도 짤 수 있음.