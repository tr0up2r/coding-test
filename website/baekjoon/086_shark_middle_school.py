n, m = map(int, input().split())  # m: 색상의 개수
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

total = 0


def bfs(x, y, group, count, target):
    queue = [(x, y)]
    group[(x, y)] = target
    visited[x][y] = True
    rainbow = []
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n or visited[nx][ny] or data[nx][ny] == -1:
                continue
            if data[nx][ny] == 0 or data[nx][ny] == target:  # 무지개 블록이나 색깔 블록이라면
                group[(nx, ny)] = data[nx][ny]
                if data[nx][ny] == 0:
                    count += 1
                    rainbow.append((nx, ny))
                queue.append((nx, ny))
                visited[nx][ny] = True
    for x, y in rainbow:
        visited[x][y] = False
    return group, count


def gravity():
    visited = [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if data[i][j] >= 0 and not visited[i][j]:
                down = [(i, j)]
                count = 0
                visited[i][j] = True
                x, y = i, j
                while True:
                    nx, ny = x+1, y
                    if nx >= n:
                        if count == 0:
                            break
                        down.reverse()
                        for k in range(len(down)):  # count만큼 내리기
                            data[down[k][0] + count][down[k][1]] = data[down[k][0]][down[k][1]]
                            data[down[k][0]][down[k][1]] = -9
                        break
                    if data[nx][ny] >= 0 and count == 0:  # 돌이라면 같이 내려갈 리스트에 추가
                        down.append((nx, ny))
                        x, y = nx, ny
                    elif data[nx][ny] == -9 and not visited[nx][ny]:
                        count += 1
                        x, y = nx, ny
                    else:
                        if count == 0:
                            break
                        down.reverse()
                        for k in range(len(down)):  # count만큼 내리기
                            data[down[k][0]+count][down[k][1]] = data[down[k][0]][down[k][1]]
                            data[down[k][0]][down[k][1]] = -9
                        break


def rotation():
    temp = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp[n-j-1][i] = data[i][j]

    for i in range(n):
        for j in range(n):
            data[i][j] = temp[i][j]
    temp.clear()


def gravity_and_rotation(xys):
    for x, y in xys:  # 그룹 있던 곳 뽑아버리고 -9로 만들기
        data[x][y] = -9
    gravity()
    rotation()
    gravity()


while True:
    visited = [[False]*n for _ in range(n)]
    groups = []
    counts = []
    max_count = -1e9
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue
            group = {}
            count = 0
            if 0 < data[i][j] <= m:
                group, count = bfs(i, j, group, count, data[i][j])
                if len(group) < 2:
                    continue
                if max_count < len(group):
                    if groups:
                        groups.clear()
                        counts.clear()
                    groups.append(group)
                    counts.append(count)
                    max_count = len(group)
                elif max_count == len(group):
                    groups.append(group)
                    counts.append(count)

    if len(groups) > 1:
        max_rainbow = -1e9
        mi = []
        for i in range(len(groups)):
            if max_rainbow < counts[i]:
                if mi:
                    mi.clear()
                max_rainbow = max(max_rainbow, counts[i])
                mi.append(i)
            elif max_rainbow == counts[i]:
                mi.append(i)
        total += len(groups[mi[len(mi)-1]])**2
        gravity_and_rotation(groups[mi[len(mi)-1]].keys())
    elif len(groups) == 1:  # 하나면 그냥 그거 구하기
        total += len(groups[0])**2
        gravity_and_rotation(groups[0].keys())
    else:  # 그룹 없으면 종료
        break

print(total)

