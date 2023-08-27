from collections import deque


n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

visited = [[False] * m for _ in range(n)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r, c):
    size = 1
    queue = deque([(r, c)])
    visited[r][c] = True

    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and arr[nr][nc]:
                size += 1
                queue.append((nr, nc))
                visited[nr][nc] = True

    return size


count, max_size = 0, 0
for r in range(n):
    for c in range(m):
        if arr[r][c] and not visited[r][c]:
            max_size = max(max_size, bfs(r, c))
            count += 1

print(count)
print(max_size)
