def solution(prices):
    answer = [0] * len(prices)

    for i in range(len(prices) - 1):
        for j in range(i, len(prices) - 1):
            answer[i] += 1
            if prices[i] > prices[j + 1]:
                break

    return answer
