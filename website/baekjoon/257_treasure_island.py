from collections import deque


m, n = map(int, input().split())
arr = []
for _ in range(m):
    arr.append(list(input()))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r, c):
    result = 0
    now = [[-1]*n for _ in range(m)]
    for x in range(m):
        for y in range(n):
            if arr[x][y] == 'L':
                now[x][y] += 1
    now[r][c] += 1
    queue = deque([(r, c)])
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < m and 0 <= nc < n and now[nr][nc] == 0:
                now[nr][nc] = now[r][c]+1
                result = max(result, now[nr][nc])
                queue.append((nr, nc))

    return result-1


answer = -1
for r in range(m):
    for c in range(n):
        flag = False
        if arr[r][c] == 'L':
            for i in range(4):
                nr, nc = r+dr[i], c+dc[i]
                if not (0 <= nr < m and 0 <= nc < n) or arr[nr][nc] == 'W':
                    flag = True
                    break
            if flag:
                answer = max(answer, bfs(r, c))

print(answer)
