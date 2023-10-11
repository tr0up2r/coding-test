from collections import deque


n, m, k = map(int, input().split())
arr = [[[0, 0, False] for _ in range(m)] for _ in range(n)]
for r in range(n):
    for c, v in enumerate(list(map(int, input().split()))):
        arr[r][c][0] = v


# 공격자 선정: 공격력이 가장 낮을 것. 가장 최근에 공격했을 것, 행열 합이 가장 클 것, 열 값이 가장 클 것.
# 피격자 선정: 공격력이 가장 높을 것, 가장 오래 전에 공격했을 것, 행열 합이 가장 작을 것, 열 값이 가장 작을 것
def get_rc(arr, opt):
    if opt == 'attacker':
        power = 1e9
    else:
        power = -1e9
    for r in range(n):
        for c in range(m):
            if opt == 'attacker':
                if arr[r][c][0] and arr[r][c][0] < power:
                    power = arr[r][c][0]
            else:
                if arr[r][c][0] > power:
                    power = arr[r][c][0]

    poss = []
    for r in range(n):
        for c in range(m):
            if arr[r][c][0] == power:
                poss.append([(r, c), arr[r][c][1]])

    if len(poss) == 1:
        return poss[0][0]
    else:
        if opt == 'attacker':
            poss.sort(key=lambda x: (x[1], -sum(x[0]), -x[0][1]))
        else:
            poss.sort(key=lambda x: (-x[1], sum(x[0]), x[0][1]))
        return poss[0][0]


def bfs(ar, ac, tr, tc):
    visited = [[False]*m for _ in range(n)]
    visited[ar][ac] = True
    queue = deque([(ar, ac, [(ar, ac)])])
    while queue:
        r, c, path = queue.popleft()
        for i in range(4):
            nr, nc = (r+dr[i])%n, (c+dc[i])%m
            if arr[nr][nc][0] != 0 and not visited[nr][nc]:
                visited[nr][nc] = True
                path.append((nr, nc))
                if nr == tr and nc == tc:
                    return path
                queue.append((nr, nc, path[:]))
                path.pop()
    return []


# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

xr = [-1, -1, -1, 0, 1, 1, 1, 0]
xc = [-1, 0, 1, 1, 1, 0, -1, -1]

while k:
    # 1. 공격자 선정
    ar, ac = get_rc(arr, 'attacker')
    # 2-1. 공격 대상 선정
    tr, tc = get_rc(arr, 'target')

    # 2-2. 공격자 공격력 증가
    arr[ar][ac][0] += n+m
    power = arr[ar][ac][0]

    # 2-3. 레이저 공격 경로 찾기
    path = bfs(ar, ac, tr, tc)
    arr[ar][ac][2] = True
    if path:
        # 2-4. 레이저 공격
        for r, c in path[1:-1]:
            arr[r][c][0] = max(0, arr[r][c][0]-(power//2))
            arr[r][c][2] = True
        arr[tr][tc][0] = max(0, arr[tr][tc][0]-power)
        arr[tr][tc][2] = True
    else:
        # 2-5. 포탄 공격
        arr[tr][tc][0] = max(0, arr[tr][tc][0]-power)
        arr[tr][tc][2] = True
        for i in range(8):
            nr, nc = (tr+xr[i])%n, (tc+xc[i])%m
            if arr[nr][nc][0] and not (nr == ar and nc == ac):
                arr[nr][nc][0] = max(0, arr[nr][nc][0]-(power//2))
                arr[nr][nc][2] = True

    # 3. 포탑 정비 & 부서지지 않은 포탑이 1개면 그 즉시 중지
    turrets = 0
    for r in range(n):
        for c in range(m):
            if arr[r][c][0]:
                turrets += 1
                if r == ar and c == ac:
                    arr[r][c][1] = 0
                else:
                    arr[r][c][1] += 1
                if arr[r][c][2]:  # 공격 연루
                    arr[r][c][2] = False
                else:
                    arr[r][c][0] += 1

    if turrets == 1:
        break
    k -= 1


max_power = -1e9
for r in range(n):
    for c in range(m):
        max_power = max(max_power, arr[r][c][0])
print(max_power)
