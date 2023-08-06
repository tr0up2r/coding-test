def solution(priorities, location):
    answer = 1

    while True:
        for i in range(len(priorities)):
            if priorities[i] == max(priorities):
                if i == location:
                    return answer
                answer += 1
                priorities[i] = -1
