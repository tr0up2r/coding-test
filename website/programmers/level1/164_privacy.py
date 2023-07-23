def solution(today, terms, privacies):
    answer = []
    d_term = dict()

    for term in terms:
        alpha, num = term.split()
        d_term[alpha] = int(num)

    for num, p in enumerate(privacies):
        d, term = p.split()
        dates = list(map(int, d.split('.')))

        dates[0] += d_term[term] // 12
        dates[1] += d_term[term] % 12

        if dates[1] > 12:
            dates[0] += 1
            dates[1] -= 12

        s_dates = '.'.join([str(dates[0]), f"{dates[1]:02}", f"{dates[2]:02}"])

        if today >= s_dates:
            answer.append(num + 1)

    return answer
