def solution(s):
    answer = [0, 0]

    while s != '1':
        before_len = len(s)
        s = s.replace('0', '')
        answer[0] += 1
        answer[1] += before_len - len(s)
        s = bin(len(s))[2:]

    return answer
