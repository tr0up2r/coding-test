from itertools import product


# product
def solution(word):
    alpha = ['A', 'E', 'I', 'O', 'U']
    answer = []
    for i in range(1, len(alpha) + 1):
        answer.extend(list(map(''.join, list(product(alpha, repeat=i)))))

    return sorted(answer).index(word) + 1


# dfs
'''
all_words = []
alpha = ['A', 'E', 'I', 'O', 'U']

def dfs(now):
    global all_words, alpha
    if now:
        all_words.append(now)
    if len(now) == 5:
        return
    for a in alpha:
        dfs(now + a)


def solution(word):
    global all_words
    dfs('')

    return all_words.index(word)+1
'''
