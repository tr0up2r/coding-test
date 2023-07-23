def solution(survey, choices):
    answer = ''

    types = {'RT': 0, 'CF': 0, 'JM': 0, 'AN': 0}

    for s, choice in zip(survey, choices):
        if s not in types:
            s = s[::-1]
            types[s] -= choice - 4
        else:
            types[s] += choice - 4

    for t in types:
        if types[t] <= 0:
            answer += t[0]
        else:
            answer += t[1]

    return answer
