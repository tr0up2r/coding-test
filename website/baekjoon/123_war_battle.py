from collections import deque

m, n = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(input()))

visited = [[False] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
w_count = []
b_count = []


def bfs(x, y, c):
    count = 1
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny] or data[nx][ny] != c:
                continue
            visited[nx][ny] = True
            count += 1
            queue.append((nx, ny))
    return count


for i in range(n):
    for j in range(m):
        if visited[i][j]:
            continue
        if data[i][j] == 'W':
            w_count.append(bfs(i, j, 'W'))
        else:
            b_count.append(bfs(i, j, 'B'))

w_answer, b_answer = 0, 0
for w in w_count:
    w_answer += w ** 2
for b in b_count:
    b_answer += b ** 2

print(w_answer, b_answer)
