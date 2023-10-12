from collections import deque


n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def get_head_tail(r, c):
    global visited
    queue = deque([(r, c)])
    while queue:
        r, c = queue.popleft()
        if arr[r][c] == 1:
            head = (r, c)
        elif arr[r][c] == 3:
            tail = (r, c)
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] and not visited[nr][nc]:
                visited[nr][nc] = True
                queue.append((nr, nc))
    return head, tail


def move(hr, hc, tr, tc, arr):
    tmp = [[0]*n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            tmp[r][c] = arr[r][c]
    queue = deque([(hr, hc)])
    team = []
    while queue:
        r, c = queue.popleft()
        if r == hr and c == hc:
            toward = {3, 4}
        else:
            toward = {-1}
        if r == tr and c == tc:
            left = 4
        else:
            left = -1

        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                if tmp[nr][nc] in toward:
                    team.append((nr, nc))
                    if (r != hr or c != hc) and tmp[r][c] == 1:
                        tmp[nr][nc] = arr[r][c]
                    else:
                        tmp[nr][nc], tmp[r][c] = arr[r][c], left
                elif arr[nr][nc] == 2 or arr[nr][nc] == 3:
                    queue.append((nr, nc))

    return tmp, team


def throw(d, x, teams):
    if d%4 == 0 or d%4 == 2:  # 좌->우 던지기 or 우->좌 던지기
        if d%4 == 0:
            start, end, v = 0, n, 1
        else:
            x = n-x-1
            start, end, v = n-1, -1, -1
        for c in range(start, end, v):
            for team in teams:
                for i in range(len(team)):
                    if (x, c) == team[i]:
                        return (i+1)**2, team

    else:  # 하->상 던지기 or 상->하 던지기
        if d%4 == 1:
            start, end, v = n-1, -1, -1
        else:
            x = n-x-1
            start, end, v = 0, n, 1
        for r in range(start, end, v):
            for team in teams:
                for i in range(len(team)):
                    if (r, x) == team[i]:
                        return (i+1)**2, team

    return 0, []


now, answer = 0, 0
while now < k:
    # 1. 머리 & 꼬리 파악
    heads, tails, visited = [], [], [[False]*n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if arr[r][c] and not visited[r][c]:
                visited[r][c] = True
                head, tail = get_head_tail(r, c)
                heads.append(head)
                tails.append(tail)


    # 2. 방향 파악
    direction = []
    for r, c in heads:
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                if arr[nr][nc] == 4:
                    if i < 2:
                        direction.append('cw')
                    else:
                        direction.append('acw')
                    break

    teams = []
    # 3. 이동 & 이동 후 순서 좌표 파악
    for (hr, hc), (tr, tc) in zip(heads, tails):
        arr, team = move(hr, hc, tr, tc, arr)
        teams.append(team)

    # 4. 공 던지기
    d, x = now//n, now%n
    score, team = throw(d, x, teams)
    answer += score

    # 5. 공을 얻은 팀이 있다면, 그 팀 방향 바꾸기
    if team:
        head, tail = team[0], team[-1]
        arr[head[0]][head[1]], arr[tail[0]][tail[1]] = 3, 1

    now += 1

print(answer)
