from collections import deque


n, m = 12, 6
arr = [list(input()) for _ in range(n)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r, c):
    global visited
    erase, count = [(r, c)], 1
    queue = deque([(r, c)])
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0 <= nr < n and 0 <= nc < m and arr[r][c] == arr[nr][nc] and not visited[nr][nc]:
                visited[nr][nc] = True
                queue.append((nr, nc))
                erase.append((nr, nc))
                count += 1

    if count >= 4:
        for er, ec in erase:
            arr[er][ec] = '.'
        return True
    return False


answer = 0
while True:
    flag = False
    visited = [[False]*m for _ in range(n)]
    for r in range(n):
        for c in range(m):
            if arr[r][c] != '.' and not visited[r][c]:
                visited[r][c] = True
                result = bfs(r, c)
                if result:
                    flag = True

    for r in range(n-1, -1, -1):
        for c in range(m-1, -1, -1):
            if arr[r][c] == '.':
                nr = r
                while True:
                    nr += -1
                    if 0 > nr:
                        break
                    elif arr[nr][c] != '.':
                        arr[nr][c], arr[r][c] = arr[r][c], arr[nr][c]
                        break

    if not flag:
        break
    answer += 1

print(answer)
