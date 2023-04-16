import sys

left = list(sys.stdin.readline().rstrip())
right = []
m = int(sys.stdin.readline())

for _ in range(m):
    c = input().split()
    if c[0] == 'L':
        if left:
            right.append(left.pop())
    elif c[0] == 'D':
        if right:
            left.append(right.pop())
    elif c[0] == 'B':
        if left:
            left.pop()
    else:
        left.append(c[1])

left.extend(reversed(right))
print(''.join(left))
