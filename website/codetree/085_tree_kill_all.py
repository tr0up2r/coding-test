n, m, k, c = map(int, input().split())  # m: 박멸 진행 년 수, k: 제초제 확산 범위, c: 제초제 남아있는 년 수
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if data[i][j] == -1:  # 벽은 -22로 치환
            data[i][j] = -22

# 상 하 좌 우
dx1 = [-1, 1, 0, 0]
dy1 = [0, 0, -1, 1]

# 좌상 좌하 우상 우하 (대각선)
dx2 = [-1, 1, -1, 1]
dy2 = [-1, -1, 1, 1]

total_kill_count = 0
trees = set()  # 나무들의 좌표
for i in range(n):
    for j in range(n):
        if data[i][j] > 0:
            trees.add((i, j))

for year in range(m):
    # 1. 인접한 곳에 나무가 있는 만큼 나무 성장
    for x, y in trees:
        if data[x][y] > 0:
            for i in range(4):
                nx = x+dx1[i]
                ny = y+dy1[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if data[nx][ny] > 0:
                    data[x][y] += 1

    # 2. 벽, 나무, 제초제 없는 칸에 번식 진행
    new_trees = []
    new_data = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_data[i][j] = data[i][j]
    for x, y in trees:
        count = 0
        t = []
        for i in range(4):
            nx = x + dx1[i]
            ny = y + dy1[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if data[nx][ny] == 0:
                t.append((nx, ny))
                count += 1
        if count != 0:
            for i, j in t:
                new_data[i][j] += data[x][y] // count
            new_trees.extend(t)

    trees.update(new_trees)
    data.clear()
    data = new_data
    max_count = -1e9
    killer = []
    for x, y in trees:
        ox, oy = x, y
        count = data[x][y]
        for i in range(4):  # 대각선으로 퍼지기
            ox, oy = x, y
            for _ in range(k):  # 확산 범위만큼 반복
                nx = ox+dx2[i]
                ny = oy+dy2[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if data[nx][ny] == -22 or data[nx][ny] == 0 or -22 < data[nx][ny] < 0:  # 벽이면 멈춤
                    break
                else:  # 나무이면
                    count += data[nx][ny]
                    ox, oy = nx, ny
        if max_count < count:
            max_count = count
            killer.clear()
            killer.append((x, y))
        elif max_count == count:
            killer.append((x, y))

    if killer:
        total_kill_count += max_count
        killer.sort()
        x, y = killer[0]
        data[x][y] = -(c+1)
        trees.remove((x, y))
        for i in range(4):
            x, y = killer[0]
            for _ in range(k):
                nx = x+dx2[i]
                ny = y+dy2[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if data[nx][ny] == -22:
                    break
                if data[nx][ny] == 0 or -22 < data[nx][ny] < 0:
                    data[nx][ny] = -(c+1)
                    break
                else:
                    data[nx][ny] = -(c+1)
                    trees.remove((nx, ny))
                    x, y = nx, ny

    for i in range(n):
        for j in range(n):
            if -22 < data[i][j] < 0:
                data[i][j] += 1

print(total_kill_count)
