import heapq as hq


def solution(operations):
    answer = []

    for op in operations:
        alpha, num = op.split()
        num = int(num)
        if alpha == 'I':
            hq.heappush(answer, num)
        elif alpha == 'D' and answer:
            if num == 1:
                answer = hq.nlargest(len(answer), answer)[1:]
                hq.heapify(answer)
            else:
                hq.heappop(answer)

    return [hq.nlargest(len(answer), answer)[0], hq.heappop(answer)] if answer else [0, 0]
