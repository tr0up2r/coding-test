from heapq import heapify, heappush, heappop


def solution(n, works):
    if sum(works) <= n:
        return 0
    works = [-1 * w for w in works]
    heapify(works)
    for _ in range(n):
        heappush(works, heappop(works) + 1)

    return sum([w ** 2 for w in works])
