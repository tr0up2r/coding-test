def solution(msg):
    answer = []
    d = dict()

    for i, w in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        d[w] = i + 1

    now = ''
    for i in range(len(msg)):
        now += msg[i]
        if now in d.keys():
            if i == len(msg) - 1:
                answer.append(d[now])
                break
            if now + msg[i + 1] not in d.keys():
                answer.append(d[now])
                d[now + msg[i + 1]] = len(d) + 1
                now = ''

    return answer
