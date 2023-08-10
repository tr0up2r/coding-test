from collections import deque


def is_correct(p):
    stack, p = [], deque(list(p))
    while p:
        now = p.popleft()
        if not stack:
            if now == ')':
                return False
            stack.append(now)
        else:
            if now == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    return False
            else:
                stack.append(now)

    if stack:
        return False
    return True


def uv_split(p):
    u, v = [], deque(p)
    counts = [0, 0]
    while True:
        now = v.popleft()
        u.append(now)
        if now == '(':
            counts[0] += 1
        else:
            counts[1] += 1
        if counts[0] == counts[1]:
            break

    return ''.join(u), ''.join(v)


def solution(p):
    if not p:
        return ''
    if is_correct(p):
        return p
    u, v = uv_split(p)
    if is_correct(u):
        return u + solution(v)
    else:
        temp = '(' + solution(v) + ')'
        u = u[1:-1]
        new_u = ''
        for b in u:
            if b == '(':
                new_u += ')'
            else:
                new_u += '('
        return temp + new_u
