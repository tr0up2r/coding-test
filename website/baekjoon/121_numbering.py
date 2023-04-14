from collections import deque

n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, list(input()))))

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False] * n for _ in range(n)]
count = []


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    now_count = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny] or data[nx][ny] == 0:
                continue
            visited[nx][ny] = True
            queue.append((nx, ny))
            now_count += 1
    return now_count


for i in range(n):
    for j in range(n):
        if data[i][j] and not visited[i][j]:
            count.append(bfs(i, j))

count.sort()
print(len(count))
for c in count:
    print(c)
