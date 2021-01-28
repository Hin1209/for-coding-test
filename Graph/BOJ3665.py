import sys
from collections import deque

input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    n = int(input().rstrip())
    # 처음 순위를 입력받는다
    rank = list(map(int, input().rstrip().split()))
    m = int(input().rstrip())
    # 자신보다 순위가 높은 팀을 저장
    bigger_than_me = [[] for _ in range(n + 1)]
    # 자신보다 순위가 낮은 팀의 개수를 저장
    cnt_small = [0] * (n + 1)

    for i in range(len(rank)):
        # tmp에 자신보다 순위가 낮은 팀들을 저장함
        tmp = rank[i + 1:]
        for j in range(len(tmp)):
            # 순위가 낮은 팀들의 bigger_than_me에 자신의 팀을 추가함
            bigger_than_me[tmp[j]].append(rank[i])
            # 순위가 낮은 팀의 개수 증가
            cnt_small[rank[i]] += 1
            
    for i in range(m):
        a, b = map(int, input().rstrip().split())
        # b와 a의 관계를 바꿔줌
        if b in bigger_than_me[a]:
            bigger_than_me[a].remove(b)
            cnt_small[b] -= 1
            bigger_than_me[b].append(a)
            cnt_small[a] += 1
        elif a in bigger_than_me[b]:
            bigger_than_me[b].remove(a)
            cnt_small[a] -= 1
            bigger_than_me[a].append(b)
            cnt_small[b] += 1

    q = deque()
    # 새로운 랭킹을 저장
    new_rank = []
    # dont_know를 판별할 변수
    check_impossible = 0
    dont_know = 0
    impossible = 1
    # 순위가 가장 낮은 팀이 존재하지 않을 경우 모순됨으로 설정
    for i in range(1, n + 1):
        if cnt_small[i] == 0:
            q.append((i, 1))
            impossible = 0
    # 자신보다 순위가 높으면서 순위가 낮은 팀의 개수가 자신보다 작거나 같으면 모순됨으로 설정
    for i in range(1, n + 1):
        for j in bigger_than_me[i]:
            if cnt_small[j] <= cnt_small[i]:
                impossible = 1

    while q:
        if impossible == 1:
            break
        now, cnt = q.popleft()
        # 모순되지는 않지만 순위가 낮은 팀의 개수가 같은 팀이 존재하는 경우 그 팀들의 순위는 결정할 수 없음
        if check_impossible == cnt:
            dont_know = 1
            break
        for i in bigger_than_me[now]:
            cnt_small[i] -= 1
            if cnt_small[i] == 0:
                q.append((i, cnt + 1))
        check_impossible = cnt
        new_rank.append(now)

    new_rank.reverse()

    if impossible:
        print("IMPOSSIBLE")
    elif dont_know:
        print("?")
    else:
        for i in range(len(new_rank)):
            print(new_rank[i], end = ' ')
        print()