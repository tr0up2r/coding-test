def solution(n, s):
    q, r = s//n, s%n
    return [q] * (n-r) + [q+1] * r if q else [-1]
