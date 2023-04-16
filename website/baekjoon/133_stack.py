n = int(input())
commands = []
for _ in range(n):
    commands.append(input().split())

stack = []
for c in commands:
    if c[0] == 'push':
        stack.append(int(c[1]))
    elif c[0] == 'pop':
        print(stack.pop() if stack else -1)
    elif c[0] == 'size':
        print(len(stack))
    elif c[0] == 'empty':
        print(0 if stack else 1)
    else:
        print(stack[len(stack) - 1] if stack else -1)
