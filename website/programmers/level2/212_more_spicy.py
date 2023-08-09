from heapq import heapify, heappush, heappop


def solution(scoville, K):
    answer = 0
    heapify(scoville)
    while True:
        min_s = heappop(scoville)
        if min_s >= K:
            break
        if not scoville:
            return -1
        heappush(scoville, (min_s + heappop(scoville) * 2))
        answer += 1

    return answer
