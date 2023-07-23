def solution(dartResult):
    answer = []
    now = ''

    dart = list(dartResult)
    d = {'S': 1, 'D': 2, 'T': 3}

    for i in range(len(dart)):
        if dart[i].isnumeric():
            now += dart[i]
        elif dart[i].isalpha():
            res = int(now) ** d[dart[i]]
            answer.append(res)
            now = ''
        else:
            if dart[i] == '*':
                answer[-2:] = [x * 2 for x in answer[-2:]]
            else:
                answer[-1] *= -1

    return sum(answer)
