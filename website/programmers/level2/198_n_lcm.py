def lcm(a, b):
    A, B = a, b
    while a % b:
        a, b = b, a % b
    return (A * B) // b


def solution(arr):
    answer = 0

    for i in range(len(arr) - 1):
        arr[i + 1] = lcm(arr[i], arr[i + 1])

    return arr[-1]
