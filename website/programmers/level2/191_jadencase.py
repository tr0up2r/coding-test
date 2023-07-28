def solution(s):
    answer = []
    words = s.split(' ')

    for word in words:
        if word == '':
            answer.append('')
        else:
            answer.append(word[0].upper() + word[1:len(word)].lower())

    return ' '.join(answer)
