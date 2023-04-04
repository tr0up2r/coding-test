n, m = map(int, input().split())  # 방의 크기

# 로봇 청소기 첫 위치와 방향
# 0: 북, 1: 동, 2: 남, 3: 서
r, c, d = map(int, input().split())

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0
while True:
    count = 0
    wall = 0
    if data[r][c] == 0:
        data[r][c] = 2  # 청소
        result += 1

    for i in range(4):
        nx = r+dx[i]
        ny = c+dy[i]
        if nx < 1 or nx >= n-1 or ny < 1 or ny >= m-1:
            wall += 1
            count += 1
            continue
        if data[nx][ny] != 0:
            count += 1

    if wall == 4:  # 사방이 벽이면
        break
    if count == 4:  # 청소 되지 않은 빈 칸이 없는 경우
        # 바라보는 방향의 반대 방향으로 전진 (후진)
        nx = r+dx[(d+2)%4]
        ny = c+dy[(d+2)%4]
        if data[nx][ny] == 1:
            break
        r, c = nx, ny

    else:  # 청소 되지 않은 빈 칸이 있는 경우
        # 반시계 방향으로 회전 (-1), 앞이 1일 때까지 반복
        for _ in range(4):
            d = (d-1)%4
            nx = r+dx[d]
            ny = c+dy[d]
            if nx < 1 or nx >= n - 1 or ny < 1 or ny >= m - 1:
                continue
            if data[nx][ny] == 0:
                r, c = nx, ny
                break

print(result)
