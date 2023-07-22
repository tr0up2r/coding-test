def solution(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(10):
        if words[i] in s:
            s = s.replace(words[i], str(i))

    return int(s)
