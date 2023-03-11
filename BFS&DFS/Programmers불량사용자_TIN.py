def select_user(selected_user, ban, match_num):
    res = set()
    if ban == len(match_num):
        tmp = tuple(sorted(selected_user))
        res.add(tmp)
        return res
    for user in match_num[ban]:
        if user in selected_user:
            continue
        else:
            selected_user.append(user)
            res |= select_user(selected_user, ban+1, match_num)
            selected_user.pop()
    return res

def solution(user_id, banned_id):
    answer = 0
    match_num = [[] for _ in range(len(banned_id))]
    for i in range(len(banned_id)):
        bad_user = banned_id[i]
        for j in range(len(user_id)):
            compare = user_id[j]
            if len(bad_user) != len(compare):
                continue
            possible = True
            for k in range(len(compare)):
                if bad_user[k] == '*':
                    continue
                if bad_user[k] != compare[k]:
                    possible = False
                    break
            if possible:
                match_num[i].append(j)
    answer = select_user([], 0, match_num)
    same_ban = dict()
    # for i in banned_id:
    #     if i not in same_ban:
    #         same_ban[i] = 1
    #     else:
    #         same_ban[i] *= (same_ban[i]+1)
    # for i in same_ban:
    #     answer //= same_ban[i]
    return len(answer)