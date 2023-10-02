from collections import deque


n = int(input())
visited = [[False]*(n+1) for _ in range(n+1)]
visited[1][0] = False

queue = deque([(1, 0, 0)])
while queue:
    now, cb, time = queue.popleft()
    if now == n:
        print(time)
        break

    for i in range(3):
        if i == 0:
            nnow, ncb = now, now
        elif i == 1:
            nnow, ncb = now+cb, cb
        else:
            nnow, ncb = now-1, cb

        if 0 <= nnow <= n and 0 <= ncb <= n and not visited[nnow][ncb]:
            visited[nnow][ncb] = True
            queue.append((nnow, ncb, time+1))
