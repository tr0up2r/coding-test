def get_num_of_divisor(n):
    result = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            result += 1
    return result + 1


def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        if get_num_of_divisor(i) % 2:
            answer -= i
        else:
            answer += i
    return answer
