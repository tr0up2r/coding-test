def solution(s):
    stack = []

    for a in s:
        if not stack or stack[-1] != a:
            stack.append(a)
        else:
            stack.pop()

    return 1 if len(stack) == 0 else 0
