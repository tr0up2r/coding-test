from collections import deque


n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

max_v = max(list(map(max, data)))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(v, r, c):
    queue = deque([(r, c)])
    visited[r][c] = True
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc] and data[nr][nc] > v:
                visited[nr][nc] = True
                queue.append((nr, nc))


answer = -1e9
for v in range(0, max_v):
    visited = [[False] * n for _ in range(n)]
    count = 0
    for r in range(n):
        for c in range(n):
            if not visited[r][c] and data[r][c] > v:
                bfs(v, r, c)
                count += 1
    answer = max(answer, count)

print(answer)
