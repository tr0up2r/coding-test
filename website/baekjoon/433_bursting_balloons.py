from collections import deque


n = int(input())
q = deque(enumerate(map(int, input().split())))
while q:
    i, now = q.popleft()
    print(i+1, end=' ')
    q.rotate(-(now-1) if now > 0 else -now)
