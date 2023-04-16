from collections import deque

n = int(input())
commands = []
for _ in range(n):
    commands.append(input().split())

queue = deque()
for c in commands:
    if c[0] == 'push_back':
        queue.append(c[1])
    elif c[0] == 'push_front':
        queue.appendleft(c[1])
    elif c[0] == 'pop_front':
        print(queue.popleft() if queue else -1)
    elif c[0] == 'pop_back':
        print(queue.pop() if queue else -1)
    elif c[0] == 'size':
        print(len(queue))
    elif c[0] == 'empty':
        print(0 if queue else 1)
    elif c[0] == 'front':
        print(queue[0] if queue else -1)
    else:
        print(queue[len(queue) - 1] if queue else -1)
