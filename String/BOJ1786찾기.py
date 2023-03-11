import sys

input = sys.stdin.readline

T = input().rstrip()
P = input().rstrip()

lps = [0] * len(P)
length = 0
i = 1
while i < len(P):
    if P[i] == P[length]:
        length += 1
        lps[i] = length
        i += 1
    else:
        if length != 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1
res = []
i = 0
j = 0
while i < len(T):
    if P[j] == T[i]:
        i += 1
        j += 1
    if j == len(P):
        res.append(i-len(P)+1)
        j = lps[j-1]
    elif i < len(T) and P[j] != T[i]:
        if j != 0:
            j = lps[j-1]
        else:
            i += 1

print(len(res))
for i in res:
    print(i, end=" ")