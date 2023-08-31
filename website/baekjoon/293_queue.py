import sys
from collections import deque


n = int(input())
queue = deque()
for _ in range(n):
    op = sys.stdin.readline().rstrip().split()
    if len(op) > 1:
        queue.append(op[1])
    else:
        now = op[0]
        if now == "pop":
            print(-1 if not queue else queue.popleft())
        elif now == "size":
            print(len(queue))
        elif now == "empty":
            print(1 if not queue else 0)
        elif now == "front":
            print(-1 if not queue else queue[0])
        else:
            print(-1 if not queue else queue[-1])
