def solution(price, money, count):
    answer = 0
    for i in range(1, count+1):
        answer += price * i
    return -(money-answer) if answer > money else 0
