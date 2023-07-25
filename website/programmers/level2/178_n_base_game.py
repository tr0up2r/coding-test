def convert(n, k):
    s = "0123456789ABCDEF"
    result = ''
    while n:
        result += s[n % k]
        n //= k

    return result[::-1]


def solution(n, t, m, p):
    result, i = '0', 1

    while len(result) < t * m:
        result += convert(i, n)
        i += 1

    answer = ''
    for i in range(t):
        answer += result[(i * m) + p - 1]

    return answer
