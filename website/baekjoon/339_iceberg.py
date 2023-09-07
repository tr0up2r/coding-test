from collections import deque


n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r, c):
    queue = deque([(r, c)])
    visited[r][c] = 1

    while queue:
        r, c = queue.popleft()
        now = [r, c, 0]
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
                if arr[nr][nc] == 0:
                    now[2] += 1
                else:
                    queue.append((nr, nc))
                    visited[nr][nc] = 1
        melt.append(now)


answer = 0
while True:
    count = 0
    melt = []
    visited = [[0] * m for _ in range(n)]
    for r in range(n):
        for c in range(m):
            if arr[r][c] > 0 and not visited[r][c]:
                count += 1
                bfs(r, c)
    for r, c, v in melt:
        arr[r][c] = max(0, arr[r][c]-v)

    if count > 1:
        break
    if sum(list(map(sum, arr))) == 0:
        answer = 0
        break
    answer += 1

print(answer)
