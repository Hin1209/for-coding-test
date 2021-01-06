def solution(food_times, k):
    answer = 0
    sum_food = sum(food_times)

    while (k != 0):
        if (k > sum(food_times)):
            answer = -1
            break
        for i in range(len(food_times)):
            if (food_times[i] != 0):
                k -= 1
                if (k == 0):
                    answer = i + 2
                    if (i == len(food_times) - 1):
                        answer = 1
                    break
                food_times[i] -= 1

    return answer