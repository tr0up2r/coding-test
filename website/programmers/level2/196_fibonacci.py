def solution(n):
    fibo = [0, 1]
    for i in range(2, n + 1):
        fibo.append(fibo[-1] + fibo[-2])

    return fibo[-1] % 1234567
