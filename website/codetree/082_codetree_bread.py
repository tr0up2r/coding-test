n, m = map(int, input().split())  # n: 격자 크기, m: 사람의 수
data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

conv_xys = []
base_xys = []
for _ in range(m):
    x, y = map(int, input().split())
    conv_xys.append((x-1, y-1))

for i in range(n):
    for j in range(n):
        if data[i][j] == 1:
            base_xys.append((i, j))

# 상 좌 우 하 (우선순위)
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]


# 편의점에 대한 베이스 캠프 최단 거리 구하기
def get_best_base_camp(x, y):
    queue = [(x, y)]
    graph = [[0]*n for _ in range(n)]
    visited[x][y] = True

    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 0 and not visited[nx][ny] and data[nx][ny] != -1:
                graph[nx][ny] = graph[x][y]+1
                visited[nx][ny] = True
                queue.append((nx, ny))

    best = 1e9
    best_xys = []
    for x, y in base_xys:
        if graph[x][y] == 0:  # 못지나가는 베이스이면 넘어가기
            continue
        best = min(best, graph[x][y])
    for x, y in base_xys:
        if graph[x][y] == best:
            best_xys.append((x, y))
    best_xys.sort()

    return best_xys[0]


def bfs(x, y, target):  # 이동해야 하는 좌표 return
    queue = [(x, y)]
    graph = [[0] * n for _ in range(n)]
    visited[x][y] = True

    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 0 and not visited[nx][ny] and data[nx][ny] != -1:
                graph[nx][ny] = graph[x][y]+1
                visited[nx][ny] = True
                queue.append((nx, ny))
        if graph[target[0]][target[1]] != 0:
            break

    all_route = []

    def dfs(x, y, route, cost):
        if cost == 1:
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                if graph[nx][ny] == 0 and visited[nx][ny]:
                    if i == 0:  # 위 -> 아래
                        i = 3
                    elif i == 1:  # 왼 -> 오
                        i = 2
                    elif i == 2:  # 오 -> 왼
                        i = 1
                    else:  # 아 -> 위
                        i = 0
                    route.append(i)
                    all_route.append(route[::-1])
                    return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n or dfs_visited[nx][ny]:
                continue
            if graph[nx][ny] != cost-1:
                continue
            if i == 0:  # 위 -> 아래
                i = 3
            elif i == 1:  # 왼 -> 오
                i = 2
            elif i == 2:  # 오 -> 왼
                i = 1
            else:  # 아 -> 위
                i = 0
            dfs_visited[nx][ny] = True
            route.append(i)
            cost -= 1
            dfs(nx, ny, route, cost)
            cost += 1
            route.pop()
            dfs_visited[nx][ny] = False


    dfs_visited = [[False]*n for _ in range(n)]
    dfs(target[0], target[1], [], graph[target[0]][target[1]])
    all_route.sort()
    return all_route[0][0]




t = 0
people_xys = {}
people = []
while True:
    t += 1  # 분 증가
    end_people = []
    # 1. 본인이 가고 싶은 편의점 방향을 향해 1칸 움직이기
    for p in people:  # 이동 중인 사람이 있으면 실행
        visited = [[False]*n for _ in range(n)]
        d = bfs(people_xys[p][0][0], people_xys[p][0][1], people_xys[p][1])
        nx = people_xys[p][0][0] + dx[d]  # 사람 좌표 갱신
        ny = people_xys[p][0][1] + dy[d]
        people_xys[p][0] = (nx, ny)
        if (nx, ny) == people_xys[p][1]:  # 2. 편의점에 도착한다면 멈춤. 그 편의점은 -1
            end_people.append(p)
            data[nx][ny] = -1
    for p in end_people:
        people.remove(p)
    if t > m and not people:
        break

    # 3. 1분에 한 명씩 사람이 나와서 베이스캠프로 들어감
    if t <= m:
        visited = [[False]*n for _ in range(n)]
        conv_x, conv_y = conv_xys.pop(0)
        x, y = get_best_base_camp(conv_x, conv_y)
        data[x][y] = -1
        people_xys[t-1] = [(x, y), (conv_x, conv_y)]  # people에 사람 좌표와, 목표 좌표 넣기
        people.append(t-1)  # 현재 이동 중인 사람

print(t)
