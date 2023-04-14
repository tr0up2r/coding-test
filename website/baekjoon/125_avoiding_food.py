from collections import deque

n, m, k = map(int, input().split())
data = [[0] * m for _ in range(n)]

for _ in range(k):
    x, y = map(int, input().split())
    data[x - 1][y - 1] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False] * m for _ in range(n)]
biggest = -1


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    count = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny] or data[nx][ny] == 0:
                continue
            visited[nx][ny] = True
            count += 1
            queue.append((nx, ny))
    return count


for d in data:
    print(d)
for i in range(n):
    for j in range(m):
        if visited[i][j] or not data[i][j]:
            continue
        biggest = max(biggest, bfs(i, j))

print(biggest)
