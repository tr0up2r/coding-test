from itertools import combinations


def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True


def solution(nums):
    answer = 0
    combs = list(combinations(nums, 3))

    for comb in combs:
        if is_prime(sum(list(comb))):
            answer += 1

    return answer
