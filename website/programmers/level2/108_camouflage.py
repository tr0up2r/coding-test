def solution(clothes):
    answer = {k: [] for _, k in clothes}
    for c, k in clothes:
        answer[k].append(c)
    result = 1
    for v in answer.values():
        result *= len(v)+1
    return result-1
