n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))
visited = [[False]*m for _ in range(n)]
biggest = -1e9

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y, count, value):
    global biggest
    if count == 4:
        biggest = max(biggest, value)
    else:
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny]:
                continue
            value += data[nx][ny]
            visited[nx][ny] = True
            count += 1
            dfs(nx, ny, count, value)
            count -= 1
            visited[nx][ny] = False
            value -= data[nx][ny]


def another_shape(x, y):
    global biggest
    for i in range(4):
        value = data[x][y]
        for j in range(3):
            k = (i+j)%4
            nx = x+dx[k]
            ny = y+dy[k]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                break
            value += data[nx][ny]
        biggest = max(biggest, value)


for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 1, data[i][j])
        visited[i][j] = False
        another_shape(i, j)

print(biggest)
