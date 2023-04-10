data = list(input())
stack = []
answer = 0
tmp = 1

for i in range(len(data)):
    if data[i] == '(':
        stack.append('(')
        tmp *= 2
    elif data[i] == '[':
        stack.append('[')
        tmp *= 3

    elif data[i] == ')':
        if not stack or stack[-1] == '[':
            answer = 0
            break
        if data[i-1] == '(':
            answer += tmp
        stack.pop()
        tmp //= 2
    else:
        if not stack or stack[-1] == '(':
            answer = 0
            break
        if data[i-1] == '[':
            answer += tmp
        stack.pop()
        tmp //= 3

if stack:
    print(0)
else:
    print(answer)
