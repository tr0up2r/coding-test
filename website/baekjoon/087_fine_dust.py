n, m, t = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

cleaner = []
for i in range(n):
    if data[i][0] == -1:
        cleaner.append((i, 0))

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def move(x, y, d):
    while True:
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or nx >= n or ny < 0 or ny >= m or data[nx][ny] == -1:
            return x, y
        temp[nx][ny] = data[x][y]
        if data[x][y - 1] == -1:  # 공기청정기 바로 앞이면
            temp[x][y] = 0
        x, y = nx, ny


for _ in range(t):  # t초 동안 반복
    # 1. 미세 먼지 확산 (동시)
    temp = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            temp[i][j] = data[i][j]

    for i in range(n):
        for j in range(m):
            if data[i][j] > 0:  # 미세먼지가 있으면 확장
                count = 0
                for k in range(4):
                    nx = i+dx[k]
                    ny = j+dy[k]
                    if nx < 0 or nx >= n or ny < 0 or ny >= m or data[nx][ny] == -1:  # 공기청정기거나 칸 없으면 확산 x
                        continue
                    temp[nx][ny] += data[i][j]//5
                    count += 1
                temp[i][j] -= ((data[i][j]//5)*count)

    for i in range(n):
        for j in range(m):
            data[i][j] = temp[i][j]
    temp.clear()

    # 2. 공기청정기 작동
    count = 0
    for x, y in cleaner:
        temp = [[0] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]
        if count == 0:  # 우 상 좌 하
            d_list = [3, 0, 2, 1]
        else:  # 우 하 좌 상
            d_list = [3, 1, 2, 0]
        y += 1
        for d in d_list:
            x, y = move(x, y, d)

        for i in range(n):
            for j in range(m):
                data[i][j] = temp[i][j]
        temp.clear()
        count += 1

result = 0
for i in range(n):
    for j in range(m):
        if data[i][j] != -1:
            result += data[i][j]

print(result)
