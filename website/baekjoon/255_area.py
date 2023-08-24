from collections import deque


m, n, k = map(int, input().split())
arr = [[0]*n for _ in range(m)]

for _ in range(k):
    c1, r1, c2, r2 = map(int, input().split())
    for r in range(r1, r2):
        for c in range(c1, c2):
            arr[r][c] = 1

answer = []
visited = [[False]*n for _ in range(m)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r, c):
    count = 0
    visited[r][c] = True
    queue = deque()
    queue.append((r, c))

    while queue:
        count += 1
        r, c = queue.popleft()

        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and arr[nr][nc] != 1:
                visited[nr][nc] = True
                queue.append((nr, nc))

    answer.append(count)


for r in range(m):
    for c in range(n):
        if arr[r][c] != 1 and not visited[r][c]:
            bfs(r, c)

answer.sort()
print(len(answer))
print(*answer)
