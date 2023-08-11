from collections import deque


t = deque(input())
p = input()
stack = []
i, now = 0, 0

while t:
    stack.append(t.popleft())
    if stack[-1] == p[-1]:
        if len(stack) >= len(p) and ''.join(stack[len(stack)-len(p):]) == p:
            for _ in range(len(p)):
                stack.pop()

answer = ''.join(stack)
if answer == p or not answer:
    print('FRULA')
else:
    print(answer)
