def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    nk = ''

    while n:
        nk += str(n % k)
        n //= k

    nk = nk[::-1].split('0')

    for num in nk:
        if num and is_prime(int(num)):
            answer += 1

    return answer
