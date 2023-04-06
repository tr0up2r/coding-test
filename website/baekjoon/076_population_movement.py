n, l, r = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = []
    queue.append((x, y))
    unions = [(x, y)]
    values = data[x][y]
    visited[x][y] = True

    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if visited[nx][ny]:
                continue

            if l <= abs(data[nx][ny] - data[x][y]) <= r:
                visited[nx][ny] = True
                unions.append((nx, ny))
                values += data[nx][ny]
                queue.append((nx, ny))

    if len(unions) == 1:
        return 0
    new_value = int(values/len(unions))
    for u in unions:
        data[u[0]][u[1]] = new_value
    return 1


result = 0
while True:
    count = 0
    visited = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                count += bfs(i, j)
    if count == 0:
        break
    result += 1

print(result)
