def is_correct(s):
    stack = []
    brackets = {')': '(', ']': '[', '}': '{'}

    for i in range(len(s)):
        if s[i] in brackets.values():
            stack.append(s[i])
        else:
            if not stack:
                return False
            else:
                if stack[-1] != brackets[s[i]]:
                    return False
                else:
                    stack.pop()
    if stack:
        return False
    return True


def solution(s):
    answer = 0

    for i in range(len(s)):
        rs = s[i:] + s[:i]
        if is_correct(rs):
            answer += 1

    return answer
