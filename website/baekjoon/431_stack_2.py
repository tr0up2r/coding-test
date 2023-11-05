import sys


stack = []
for _ in range(int(input())):
    x = list(map(int, sys.stdin.readline().rstrip().split()))
    if x[0] == 1:
        stack.append(x[1])
    elif x[0] == 2:
        print(stack.pop()) if stack else print(-1)
    elif x[0] == 3:
        print(len(stack))
    elif x[0] == 4:
        print(0) if stack else print(1)
    else:
        print(stack[-1]) if stack else print(-1)
