import sys

input = sys.stdin.readline
# 테스트 케이스 개수
T = int(input())
# 테스트 케이스 만큼 반복
for _ in range(T):
    N, K = map(int, input().split())
    # 빌딩을 짓는데 걸리는 시간
    building = [0] * (N + 1)
    # 인덱스의 빌딩을 짓기 이전에 지어야 하는 빌딩
    previous_building = [[] for _ in range(N + 1)]
    # 각 빌딩을 짓는데 걸리는 시간
    build_time = list(map(int, input().split()))
    for i in range(K):
        pre, build = map(int, input().split())
        previous_building[build].append(pre)
    # 이기기 위해 지어야 하는 건물의 번호
    win = int(input())
    # 반복문이 처음임을 설정하는 변수
    first = 1
    # 이미 지어진 건물을 제외하고 남은 건물의 번호
    can_build = [i for i in range(1, N + 1)]

    while building[win] == 0:
        # 반복문이 처음인 경우, 먼저 지어야 하는 건물이 없는 건물을 지어준다.
        if first == 1:
            # 다음부터는 반복문이 처음이 아니므로 0으로 설정
            first = 0
            for i in range(1, len(previous_building)):
                if len(previous_building[i]) == 0:
                    building[i] = build_time[i-1]
                    # 건물을 짓고나서 지을수 있는 건물 리스트에서 지워준다
                    can_build.remove(i)
        # 지을 수 있는 건물에 대해서만 검사
        for i in can_build:
            # 건물을 지을 수 있는지를 표현하는 변수
            possible_build = 1
            # 건물을 짓는데 걸리는 시간
            total_time = 0
            # j는 미리 지어야 하는 건물의 번호
            for j in previous_building[i]:
                # 미리 지어야 하는 건물이 아직 지어지지 않았으면 possible_build를 0으로 설정하고 반복문 종료
                if j in can_build:
                    possible_build = 0
                    break
                # 먼저 지어야 하는 건물을 짓는데 걸리는 시간 중 가장 오래 걸리는 경우를 선택
                if total_time < building[j]:
                    total_time = building[j]
            # 건물을 지을 수 있으면 건물을 짓는데 걸리는 시간의 최댓값으로 초기화 시켜주고, 지을 수 있는 건물 리스트에서 건물을 뺀다.
            if possible_build:
                building[i] = max(building[i], total_time + build_time[i-1])
                can_build.remove(i)
        # 지을 수 있는 건물이 더 이상 남아있지 않으면 반복문 종료
        if len(can_build) == 0:
            break
    # 이기기 위해 지어야 하는 건물을 짓는데 걸리는 시간을 출력한다.
    print(building[win])
