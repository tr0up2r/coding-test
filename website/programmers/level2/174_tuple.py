from collections import Counter


def solution(s):
    answer = sorted(list(map(int, s.replace('{', '').replace('}', '').split(','))))
    return list(map(lambda x: x[0], sorted(Counter(answer).items(), key=lambda x: x[1], reverse=True)))
