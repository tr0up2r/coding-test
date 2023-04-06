n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

# 초기 아기 상어의 크기
size = 2
# 자신의 크기와 동일한 수만큼의 물고기를 먹어야 size += 1
eat_count = 0
time = 0

for i in range(n):
    for j in range(n):
        if data[i][j] == 9:
            shark_idx = [i, j]
            break

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = []
    queue.append([x, y])

    graph = [[0]*n for _ in range(n)]

    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if data[nx][ny] > size:
                continue

            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append([nx, ny])

    return graph


while True:
    fish_idxs = []
    # 1. 더 먹을 물고기가 없다면 종료
    if sum(map(sum, data)) == 9:
        break
    graph = bfs(shark_idx[0], shark_idx[1])

    count = 0
    for i in range(n):
        for j in range(n):
            if 0 < data[i][j] < 7 and data[i][j] < size:
                cost = graph[i][j]
                if cost == 0:
                    continue
                fish_idxs.append([graph[i][j], [i, j]])

    # 접근할 수 있는 물고기가 없다면
    if not fish_idxs:
        break

    # 2. 먹을 수 있는 물고기가 1마리라면 그 물고기를 먹으러 간다
    if count == 1:
        print(fish_idxs)
        time += fish_idxs[0][0]
        data[shark_idx[0]][shark_idx[1]] = 0
        shark_idx = fish_idxs[0][1]
        data[shark_idx[0]][shark_idx[1]] = 9
        eat_count += 1
        if size == eat_count:
            size += 1
            eat_count = 0

        fish_idxs.clear()
        continue

    # 3. 1마리보다 많다면, 거리가 가장 가까운 물고기로
    fish_idxs.sort()
    time += fish_idxs[0][0]
    data[shark_idx[0]][shark_idx[1]] = 0
    shark_idx = fish_idxs[0][1]
    data[shark_idx[0]][shark_idx[1]] = 9
    eat_count += 1
    if size == eat_count:
        size += 1
        eat_count = 0

    fish_idxs.clear()

print(time)
