from collections import Counter


def solution(topping):
    answer = 0
    me = Counter(topping)
    bro = set()

    for t in topping:
        me[t] -= 1
        if me[t] == 0:
            del me[t]
        bro.add(t)

        if len(me) < len(bro):
            return answer

        if len(me) == len(bro):
            answer += 1
