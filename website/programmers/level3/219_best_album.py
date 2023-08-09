def solution(genres, plays):
    d = dict()
    answer = []

    for g, p in zip(genres, plays):
        if g not in d.keys():
            d[g] = p
        else:
            d[g] += p
    sorted_g = list(map(lambda x: x[0], sorted(d.items(), key=lambda x: x[1], reverse=True)))

    result = []
    for i in range(len(genres)):
        result.append([i, genres[i], plays[i]])
    result.sort(key=lambda x: x[2], reverse=True)

    for g in sorted_g:
        now = 0
        for r in result:
            if now == 2:
                break
            if r[1] == g:
                answer.append(r[0])
                now += 1

    return answer
