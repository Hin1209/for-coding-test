def search(map, start, num_dist, cnt, re_cnt, first, first_index=0):
    cnt -= 1
    re_cnt += 1
    for st in range(start, len(map)):
        tmp = []
        for i in map:
            tmp.append(i)
        if st + num_dist[re_cnt] < len(map):
            for i in range(st, st + num_dist[re_cnt]):
                tmp[i] = 0
            next_index = st+num_dist[re_cnt]
        elif st + num_dist[re_cnt] >= len(map):
            for i in range(st, len(map)):
                tmp[i] = 0
            for i in range(st+num_dist[re_cnt]-len(map)):
                tmp[i] = 0
            next_index = st+num_dist[re_cnt]-len(map)
        if first == 1:
            first_index = st
        if cnt > 0:
            search(tmp, next_index, num_dist, cnt, re_cnt, first-1, first_index)
        elif cnt == 0:
            for j in range(len(map)):
                if map[j] == 1 and st :
                    return False
            return True




def solution(n, weak, dist):
    answer = 0
    mapp = [0 for _ in range(n)]
    dist.sort(reverse=True)
    for w in weak:
        mapp[w] = 1
    for i in range(1, len(dist)+1):
        if search(mapp, 0, dist, i, -1, 1, 0):
            answer = i
            break
        else:
            answer = -1

    return answer
print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))