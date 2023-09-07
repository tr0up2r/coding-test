from collections import deque


n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r, c):
    queue = deque([(r, c)])
    visited[r][c] = True
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc]:
                if arr[nr][nc] >= 1:
                    arr[nr][nc] += 1
                    melt.add((nr, nc))
                else:
                    visited[nr][nc] = 1
                    queue.append((nr, nc))


answer = 0
melt = []
while True:
    visited = [[0]*m for _ in range(n)]
    melt = set()
    bfs(0, 0)
    answer += 1
    for r, c in melt:
        if arr[r][c] >= 3:
            arr[r][c] = 0
        else:
            arr[r][c] = 1
    if sum(list(map(sum, arr))) == 0:
        break

print(answer)
