from collections import deque


n = int(input())
arr = []
for _ in range(n):
    arr.append(list(input()))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

normal = {'R': ['R'], 'G': ['G'], 'B': ['B']}
weak = {'R': ['R', 'G'], 'G': ['R', 'G'], 'B': ['B']}


def bfs(r, c, d):
    queue = deque([(r, c)])
    visited[r][c] = True

    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and arr[nr][nc] in d[arr[r][c]]:
                visited[nr][nc] = True
                queue.append((nr, nc))


option = [normal, weak]
for op in option:
    count = 0
    visited = [[False] * n for _ in range(n)]

    for r in range(n):
        for c in range(n):
            if not visited[r][c]:
                bfs(r, c, op)
                count += 1

    print(count, end=' ')
