def solution(elements):
    # ver. 1
    answer = set(elements)

    for i in range(0, len(elements)):
        s = 0
        for j in range(i, i + len(elements)):
            s += elements[j % len(elements)]
            answer.add(s)

    return len(answer)

    # ver. 2
    '''
    answer = set(elements)
    len_e = len(elements)
    elements *= 2

    for i in range(2, len_e+1):
        for j in range(0, len_e):
            answer.add(sum(elements[j:j+i]))

    return len(answer)
    '''
