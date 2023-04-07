n = int(input())
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))
half = n//2

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
perm_size = 2
groups = []


def bfs(x, y):
    group = [(x, y)]
    queue = [(x, y)]
    visited[x][y] = True

    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny]:
                continue
            if data[nx][ny] == data[x][y]:  # 같은 그룹
                group.append((nx, ny))
                queue.append((nx, ny))
                visited[nx][ny] = True

    return set(group), data[group[0][0]][group[0][1]]


def get_perm(idx, now_list, n):
    if len(now_list) == perm_size:
        perm_list.append(now_list[:])

    for i in range(idx, n):
        get_perm(i+1, now_list+[perm[i]], n)


def get_score(g1, g2, value1, value2):
    face = 0
    for x in range(n):
        for y in range(n):
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if (x, y) in g1 and (nx, ny) in g2:
                    face += 1

    if face == 0:
        return 0
    b1, b2 = len(g1), len(g2)  # 칸 수
    return (b1 + b2) * value1 * value2 * face


def plus_rotation():
    for i in range(n):
        for j in range(n):
            if i == half or j == half:
                temp[i][j] = data[j][n-1-i]


def remain_rotation(x, y, l):
    for i in range(x, x+l):
        for j in range(y, y+l):
            ox, oy = i-x, j-y
            rx, ry = oy, l-ox-1
            temp[rx+x][ry+y] = data[i][j]


total = 0
for _ in range(4):  # 3회전 이후 예술 점수
    visited = [[False]*n for _ in range(n)]
    groups = []
    values = []

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                group, value = bfs(i, j)
                groups.append(group)
                values.append(value)

    perm_list = []
    perm = [i for i in range(len(groups))]
    get_perm(0, [], len(groups))
    for i, j in perm_list:
        total += get_score(groups[i], groups[j], values[i], values[j])

    temp = [[0]*n for _ in range(n)]
    plus_rotation()
    remain_rotation(0, 0, half)
    remain_rotation(0, half+1, half)
    remain_rotation(half+1, 0, half)
    remain_rotation(half+1, half+1, half)

    for i in range(n):
        for j in range(n):
            data[i][j] = temp[i][j]
    temp.clear()

print(total)
