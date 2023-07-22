def solution(n):
    conv, answer = '', 0

    while n:
        conv += str(n % 3)
        n //= 3

    for i in range(len(conv)):
        answer += int(conv[len(conv) - 1 - i]) * 3 ** i

    return answer
