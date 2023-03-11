import sys
from collections import deque

input = sys.stdin.readline

peo, par = map(int, input().split())
know = list(map(int, input().split()))
know = know[1:]

deq = deque()

for i in range(len(know)):
    deq.append(know[i])

party = []
for i in range(par):
    tmp = list(map(int, input().split()))
    party.append(tmp[1:])
check_know = [0] * (peo+1)
true_party = [0] * par
while deq:
    target = deq.popleft()
    for i in range(par):
        if target in party[i]:
            true_party[i] = 1
            for j in range(len(party[i])):
                if not check_know[party[i][j]]:
                    check_know[party[i][j]] = 1
                    deq.append(party[i][j])
count = 0

for i in range(par):
    if not true_party[i]:
        count += 1
        
print(count)