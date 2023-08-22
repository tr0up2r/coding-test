from collections import deque


t = int(input())
stack = []

for _ in range(t):
    b = deque(input())
    answer = 'YES'

    while b:
        now = b.popleft()
        if not stack:
            stack.append(now)
        else:
            if stack[-1] == '(' and now == ')':
                stack.pop()
            else:
                stack.append(now)

    if stack:
        answer = 'NO'
    print(answer)

    stack.clear()
