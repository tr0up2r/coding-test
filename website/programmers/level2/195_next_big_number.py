def solution(n):
    one = bin(n).count('1')
    answer = n+1
    while True:
        if one == bin(answer).count('1'):
            return answer
        answer += 1
