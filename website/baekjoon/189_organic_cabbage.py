from collections import deque

t = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r, c):
    queue = deque()
    queue.append((r, c))
    data[r][c] = 0

    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if nr < 0 or nr >= n or nc < 0 or nc >= m or data[nr][nc] == 0:
                continue
            queue.append((nr, nc))
            data[nr][nc] = 0


for _ in range(t):
    m, n, k = map(int, input().split())
    data = [[0] * m for _ in range(n)]

    for _ in range(k):
        c, r = map(int, input().split())
        data[r][c] = 1

    count = 0

    for r in range(n):
        for c in range(m):
            if data[r][c]:
                bfs(r, c)
                count += 1

    print(count)
