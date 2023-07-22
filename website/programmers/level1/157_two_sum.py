from itertools import combinations


def solution(numbers):
    answer = set()
    combs = list(combinations(numbers, 2))

    for comb in combs:
        answer.add(sum(list(comb)))

    return sorted(list(answer))
