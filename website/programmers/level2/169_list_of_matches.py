def solution(n,a,b):
    answer = 1
    if a > b:
        a, b = b, a

    while not (b-a == 1 and a%2):
        a, b = a//2+1 if a % 2 else a//2, b//2+1 if b%2 else b//2
        answer += 1

    return answer
