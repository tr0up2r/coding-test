import sys
from collections import deque


q = deque()
for _ in range(int(input())):
    ops = sys.stdin.readline().rstrip().split()
    if len(ops) == 2:
        q.append(int(ops[1]))
    else:
        op = ops[0]
        if op == 'pop':
            print(q.popleft() if q else -1)
        elif op == 'size':
            print(len(q))
        elif op == 'empty':
            print(0 if q else 1)
        elif op == 'front':
            print(q[0] if q else -1)
        else:
            print(q[-1] if q else -1)
