def solution(n):
    answer = ''

    while n:
        r = n % 3
        if not r:
            r = 4
            n -= 1
        answer += str(r)
        n //= 3

    return answer[::-1]
