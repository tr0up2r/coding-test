def solution(d, budget):
    s, answer = 0, 0
    d.sort()

    for i in range(len(d)):
        s += d[i]
        if s > budget:
            break
        answer += 1
    return answer
