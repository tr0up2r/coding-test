def solution(n):
    answer = 0

    for i in range(1, n // 2 + 1):
        s = i
        for j in range(i + 1, n):
            s += j
            if s == n:
                answer += 1
                break
            if s > n:
                break

    answer += 1

    return answer
