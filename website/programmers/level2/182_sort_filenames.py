def solution(files):
    sort_result, answer = [], []
    d = dict()

    for i in range(len(files)):
        d[i] = files[i]

        flag = False
        letters, digits = '', ''

        for s in files[i]:
            if s.isdigit() and len(digits) < 5:
                flag = True
                digits += s
            else:
                if flag:
                    break
                letters += s
        sort_result.append([i, letters, int(digits)])

    sort_result.sort(key=lambda x: (x[1].lower(), x[2], x[0]))

    for res in sort_result:
        answer.append(d[res[0]])

    return answer
