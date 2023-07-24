def solution(n, words):
    answer = [0, 0]
    before_words = {words[0]}

    for i in range(1, len(words)):
        if words[i - 1][-1] == words[i][0] and words[i] not in before_words:
            before_words.add(words[i])
        else:
            answer[0], answer[1] = i % n + 1, i // n + 1
            break

    return answer
