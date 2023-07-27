from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    combs = []

    for c in course:
        for order in orders:
            if len(order) < c:
                continue
            combs.extend(combinations(sorted(order), c))

        counter = Counter(combs)
        max_count = -1e9
        for key, value in counter.most_common():
            if value >= max_count and value > 1:
                max_count = value
                answer.append(''.join(list(key)))
            else:
                break

        combs.clear()

    return sorted(answer)
