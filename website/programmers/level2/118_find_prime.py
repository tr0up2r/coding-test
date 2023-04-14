from itertools import permutations


def solution(numbers):
    def is_prime(n):
        if n <= 1:
            return False
        elif n < 4:
            return True
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True

    answer = 0
    numbers = list(numbers)
    perms = []
    for i in range(1, len(numbers) + 1):
        perms.extend(map(int, map(''.join, map(list, permutations(numbers, i)))))

    perms = set(perms)

    for perm in perms:
        if is_prime(perm):
            answer += 1

    return answer
