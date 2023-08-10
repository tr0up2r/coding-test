def get_time(start, end):
    s_h, s_m = map(int, start.split(':'))
    e_h, e_m = map(int, end.split(':'))

    return (e_h * 60 + e_m) - (s_h * 60 + s_m)


def solution(m, musicinfos):
    answer = []
    m = m.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')

    for idx, info in enumerate(musicinfos):
        info_list = info.split(',')
        playtime = get_time(info_list[0], info_list[1])

        info_list[3] = info_list[3].replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace(
            'A#', 'a')
        info_list[3] = (info_list[3] * max(1, playtime // len(info_list[3]) + 1))[:playtime]

        if m in info_list[3]:
            answer.append((idx, info_list[2], playtime))

    if not answer:
        return '(None)'

    answer.sort(key=lambda x: (x[2], -x[0]))
    return answer[-1][1]
