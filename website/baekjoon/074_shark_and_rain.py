n, m = map(int, input().split())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

dss = []
for _ in range(m):
    dss.append(list(map(int, input().split())))

# 초기 구름
clouds = [[n-1, 0], [n-1, 1], [n-2, 0], [n-2, 1]]

# 8방 (1부터 들어오니까 앞 하나 비우기)
# 대각선은 2, 4, 6, 8
dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]

for ds in dss:
    visited = [[False]*n for _ in range(n)]
    # 1. 모든 구름을 d 방향으로 s칸 이동
    for cloud in clouds:
        nx = (cloud[0] + (dx[ds[0]]*ds[1])) % n
        ny = (cloud[1] + (dy[ds[0]]*ds[1])) % n
        cloud[0], cloud[1] = nx, ny
        visited[nx][ny] = True
        # 2. 구름 칸 비내리기 (+1)
        data[nx][ny] += 1

    # 3. 구름 사라진다
    old_clouds = clouds.copy()
    clouds.clear()

    for bug in old_clouds:
        for i in range(2, 9, 2):
            nx = bug[0] + dx[i]
            ny = bug[1] + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if data[nx][ny] > 0:
                data[bug[0]][bug[1]] += 1

    for i in range(n):
        for j in range(n):
            if data[i][j] >= 2 and not visited[i][j]:
                data[i][j] -= 2
                clouds.append([i, j])

print(sum(list(map(sum, data))))
