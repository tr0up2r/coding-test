def solution(sequence, k):
    answer = []
    l, r = 0, -1
    now_sum = 0

    while True:
        if now_sum < k:
            r += 1
            if r >= len(sequence):
                break
            now_sum += sequence[r]
        else:
            now_sum -= sequence[l]
            if l >= len(sequence):
                break
            l += 1
        if now_sum == k:
            answer.append([l, r])

    answer.sort(key=lambda x: (x[1] - x[0], x[0]))

    return answer[0]
