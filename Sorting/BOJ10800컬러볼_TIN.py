import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
color_sum = [0] * (200001)
balls = []
identify_ball = {}
can_win = [0] * n
sum = 0

for i in range(n):
    color, size = map(int, input().split())
    balls.append((size, color))
    if f"{size},{color}" not in identify_ball.keys():
        identify_ball[f"{size},{color}"] = [i]
    else:
        identify_ball[f"{size},{color}"].append(i)
    
balls.sort()
pre_size = 0
same_size = 0
same_color = 0
same_col_cnt = 0
for i in range(n):
    bs, bc = balls[i]
    index = identify_ball[f"{bs},{bc}"]
    if pre_size == bs:
        same_size += 1    
        if bc == same_color:
            same_col_cnt += 1
            for ind in index:
                can_win[ind] = sum - color_sum[bc] - (same_size - same_col_cnt) * pre_size 
        else:
            for ind in index:
                can_win[ind] = sum - color_sum[bc] - same_size * pre_size
            same_col_cnt = 0
        sum += bs
        color_sum[bc] += bs 
        same_color = bc
        continue
    for ind in index:
        can_win[ind] = sum - color_sum[bc]    
    sum += bs
    color_sum[bc] += bs
    pre_size = bs
    same_size = 0
    same_color = bc
    same_col_cnt = 0

for i in range(n):
    print(can_win[i])
    
    