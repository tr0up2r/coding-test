def solution(record):
    answer, user_info = [], dict()

    for r in record:
        info = r.split()
        if info[0] == 'Enter':
            answer.append(info[1] + "님이 들어왔습니다.")
            user_info[info[1]] = info[2]
        elif info[0] == 'Leave':
            answer.append(info[1] + "님이 나갔습니다.")
        else:
            user_info[info[1]] = info[2]

    for i in range(len(answer)):
        answer[i] = user_info[answer[i].split('님')[0]] + answer[i][len(answer[i].split('님')[0]):]

    return answer
