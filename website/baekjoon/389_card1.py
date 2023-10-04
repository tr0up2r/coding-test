from collections import deque


q = deque(list(range(1, int(input())+1)))
while q:
    print(q.popleft(), end=' ')
    if q:
        q.append(q.popleft())
