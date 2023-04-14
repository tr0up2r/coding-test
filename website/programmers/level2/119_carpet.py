def solution(brown, yellow):
    answer = []

    for i in range(1, yellow + 1):
        if yellow % i == 0:
            h, w = i, yellow // i
            if h * 2 + w * 2 + 4 == brown:
                return sorted([h + 2, w + 2], reverse=True)

    return answer
