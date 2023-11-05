from collections import deque


n = int(input())
row = deque(map(int, input().split()))
stack, i = [], 1
while row:
    now = row.popleft()
    if now == i:
        i += 1
    else:
        stack.append(now)
    while stack:
        if stack[-1] == i:
            stack.pop()
            i += 1
        else:
            break

print('Nice') if not stack else print('Sad')
