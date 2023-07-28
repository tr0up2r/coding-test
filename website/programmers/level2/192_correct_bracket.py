def solution(s):
    answer = True
    stack = []

    for b in s:
        if not stack:
            if b == ')':
                return False
            stack.append(b)
        else:
            if stack[-1] == '(' and b == ')':
                stack.pop()
                continue
            stack.append(b)

    return len(stack) == 0
