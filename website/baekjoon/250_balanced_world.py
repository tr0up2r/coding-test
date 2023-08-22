from collections import deque


stack = []
b = {')': '(', ']': '['}

while True:
    s = input()
    if s == '.':
        break

    s = deque(s)
    while s:
        now = s.popleft()
        if now == '(' or now == ')' or now == '[' or now == ']':
            if not stack:
                stack.append(now)
            else:
                if now in b.keys():
                    if stack[-1] == b[now]:
                        stack.pop()
                    else:
                        stack.append(now)
                else:
                    stack.append(now)
    if stack:
        print('no')
    else:
        print('yes')

    stack.clear()
