from collections import Counter


def solution(k, tangerine):
    answer, goal = 0, 0
    count = Counter(tangerine).most_common()

    for key, value in count:
        goal += value
        answer += 1
        if goal >= k:
            break

    return answer
